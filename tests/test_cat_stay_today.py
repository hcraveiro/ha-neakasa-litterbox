"""Daily cat visit durations and their sensor contract."""

from __future__ import annotations

from dataclasses import replace
from datetime import UTC, datetime
from unittest.mock import MagicMock

import pytest
from homeassistant.components.sensor import SensorDeviceClass, SensorStateClass
from homeassistant.const import UnitOfTime
from homeassistant.helpers import entity_registry as er
from homeassistant.util import dt as dt_util
from neakasa_litterbox_sdk import RecordType

from custom_components.neakasa_litterbox.coordinator import _build_snapshot
from custom_components.neakasa_litterbox.data import NeakasaPayload
from custom_components.neakasa_litterbox.sensor.cat_stay_today import (
    NeakasaCatStayTodaySensor,
)


@pytest.fixture
def local_day(freezer, verify_cleanup):
    timezone = dt_util.get_time_zone("Europe/Lisbon")
    dt_util.set_default_time_zone(timezone)
    freezer.move_to(datetime(2026, 10, 24, 12, tzinfo=UTC))
    yield int(dt_util.start_of_local_day().timestamp())
    dt_util.set_default_time_zone(UTC)


def test_stay_sums_only_this_cats_completed_visits(
    local_day, sample_device, sample_status, sample_cat, sample_record
):
    visit = replace(sample_record, start_time=local_day + 60, end_time=local_day + 105)
    second_visit = replace(
        visit, record_id=2, start_time=local_day + 120, end_time=local_day + 150
    )
    other_cat = replace(sample_cat, id=43, name="Other cat")
    other_visit = replace(visit, record_id=3, cat_id=other_cat.id)
    cleaning = replace(visit, record_id=4, record_type=RecordType.CLEAN_CYCLE)
    snap = _build_snapshot(
        sample_device,
        sample_status,
        [sample_cat, other_cat],
        [visit, second_visit, other_visit, cleaning],
    )

    assert snap.cat_stats[sample_cat.id]["stay_today_seconds"] == 75
    assert snap.cat_stats[other_cat.id]["stay_today_seconds"] == 45


@pytest.mark.parametrize(
    ("start_offset", "end_offset", "expected"),
    [
        (-50, 20, 20),
        (-50, 0, 0),
        (-100, -50, 0),
        (10, 10, 0),
        (20, 10, 0),
        (10, 0, 0),
        (10, 100_000, 0),
    ],
)
def test_stay_clips_at_local_midnight_and_ignores_invalid_or_future_durations(
    local_day,
    sample_device,
    sample_status,
    sample_cat,
    sample_record,
    start_offset,
    end_offset,
    expected,
):
    visit = replace(
        sample_record,
        start_time=local_day + start_offset,
        end_time=local_day + end_offset,
    )
    snap = _build_snapshot(sample_device, sample_status, [sample_cat], [visit])

    assert snap.cat_stats[sample_cat.id]["stay_today_seconds"] == expected


def test_stay_is_zero_without_records(sample_device, sample_status, sample_cat):
    snap = _build_snapshot(sample_device, sample_status, [sample_cat], [])
    assert snap.cat_stats[sample_cat.id]["stay_today_seconds"] == 0


def test_stay_resets_on_next_local_day(
    local_day, sample_device, sample_status, sample_cat, sample_record, freezer
):
    visit = replace(sample_record, start_time=local_day + 60, end_time=local_day + 105)
    before = _build_snapshot(sample_device, sample_status, [sample_cat], [visit])
    freezer.move_to(datetime(2026, 10, 25, 12, tzinfo=UTC))
    after = _build_snapshot(sample_device, sample_status, [sample_cat], [visit])

    assert before.cat_stats[sample_cat.id]["stay_today_seconds"] == 45
    assert after.cat_stats[sample_cat.id]["stay_today_seconds"] == 0


@pytest.mark.parametrize(
    "day",
    [datetime(2026, 3, 29, 12, tzinfo=UTC), datetime(2026, 10, 25, 12, tzinfo=UTC)],
)
def test_stay_uses_local_midnight_on_daylight_saving_transition(
    day, local_day, sample_device, sample_status, sample_cat, sample_record, freezer
):
    freezer.move_to(day)
    midnight = int(dt_util.start_of_local_day().timestamp())
    visit = replace(sample_record, start_time=midnight - 50, end_time=midnight + 20)
    snap = _build_snapshot(sample_device, sample_status, [sample_cat], [visit])

    assert snap.cat_stats[sample_cat.id]["stay_today_seconds"] == 20


def test_stay_sensor_contract(
    local_day, sample_device, sample_status, sample_cat, sample_record
):
    visit = replace(sample_record, start_time=local_day + 60, end_time=local_day + 105)
    snap = _build_snapshot(sample_device, sample_status, [sample_cat], [visit])
    coordinator = MagicMock()
    coordinator.data = NeakasaPayload(devices={sample_device.iot_id: snap})
    sensor = NeakasaCatStayTodaySensor(coordinator, sample_device.iot_id, sample_cat.id)

    assert sensor.native_value == 45
    assert sensor.unique_id == f"{sample_device.iot_id}_cat_{sample_cat.id}_stay_today"
    assert sensor.translation_key == "cat_stay_today"
    assert sensor.native_unit_of_measurement == UnitOfTime.SECONDS
    assert sensor.device_class == SensorDeviceClass.DURATION
    assert sensor.state_class == SensorStateClass.TOTAL_INCREASING


@pytest.mark.parametrize("missing", ["payload", "device", "stats"])
def test_stay_sensor_returns_none_when_data_missing(
    missing, sample_device, sample_status, sample_cat
):
    snap = _build_snapshot(sample_device, sample_status, [sample_cat], [])
    coordinator = MagicMock()
    coordinator.data = None
    if missing == "device":
        coordinator.data = NeakasaPayload(devices={})
    elif missing == "stats":
        coordinator.data = NeakasaPayload(
            devices={sample_device.iot_id: replace(snap, cat_stats={})}
        )
    sensor = NeakasaCatStayTodaySensor(coordinator, sample_device.iot_id, sample_cat.id)

    assert sensor.native_value is None


async def test_stay_sensor_registered_with_translated_name(
    hass, setup_integration, sample_device, sample_cat
):
    registry = er.async_get(hass)
    entity_id = registry.async_get_entity_id(
        "sensor",
        "neakasa_litterbox",
        f"{sample_device.iot_id}_cat_{sample_cat.id}_stay_today",
    )
    assert entity_id is not None
    state = hass.states.get(entity_id)
    assert state is not None
    assert state.state == "0"
    assert state.attributes["friendly_name"] == f"{sample_cat.name} Stay today"
    assert state.attributes["device_class"] == "duration"
    assert state.attributes["state_class"] == "total_increasing"
    assert state.attributes["unit_of_measurement"] == "s"
