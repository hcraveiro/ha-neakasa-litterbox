from __future__ import annotations

import dataclasses
from dataclasses import replace
from datetime import UTC, datetime
from unittest.mock import MagicMock

import pytest
from homeassistant.components.sensor import SensorDeviceClass, SensorStateClass
from homeassistant.const import UnitOfMass, UnitOfTime
from homeassistant.helpers import entity_registry as er
from homeassistant.util import dt as dt_util
from neakasa_litterbox_sdk import OperatingState, RecordType

from custom_components.neakasa_litterbox.coordinator import _build_snapshot
from custom_components.neakasa_litterbox.data import (
    NeakasaDeviceSnapshot,
    NeakasaPayload,
)
from custom_components.neakasa_litterbox.sensor.cat_last_visit import (
    NeakasaCatLastVisitSensor,
)
from custom_components.neakasa_litterbox.sensor.cat_time_in_box_today import (
    NeakasaCatTimeInBoxTodaySensor,
)
from custom_components.neakasa_litterbox.sensor.cat_visits_today import (
    NeakasaCatVisitsTodaySensor,
)
from custom_components.neakasa_litterbox.sensor.cat_weight import NeakasaCatWeightSensor
from custom_components.neakasa_litterbox.sensor.last_visit import NeakasaLastVisitSensor
from custom_components.neakasa_litterbox.sensor.operating_state import (
    NeakasaOperatingStateSensor,
)
from custom_components.neakasa_litterbox.sensor.sand_percent import (
    NeakasaSandPercentSensor,
)
from custom_components.neakasa_litterbox.sensor.visits_today import (
    NeakasaVisitsTodaySensor,
)


def _coord_with(snap: NeakasaDeviceSnapshot) -> MagicMock:
    coord = MagicMock()
    coord.data = NeakasaPayload(devices={snap.device["iot_id"]: snap})
    coord.last_update_success = True
    return coord


def _make_snapshot(
    sample_device,
    sample_status,
    sample_cat,
    *,
    visits_today=2,
    last_visit_at=1_700_000_500,
    cat_stats=None,
) -> NeakasaDeviceSnapshot:
    if cat_stats is None:
        cat_stats = {
            sample_cat.id: {
                "last_visit_at": 1_700_000_500,
                "last_visit_weight": 4.65,
                "last_visit_weight_unit": "kg",
                "visits_today": 3,
                "time_in_box_today_seconds": 75,
            },
        }
    return NeakasaDeviceSnapshot(
        device={
            "iot_id": sample_device.iot_id,
            "device_name": sample_device.device_name,
            "product_name": sample_device.product_name,
            "firmware_version": sample_status.firmware_version,
            "hardware_version": sample_status.hardware_version,
        },
        status=sample_status,
        cats=(sample_cat,),
        visits_today=visits_today,
        last_visit_at=last_visit_at,
        cat_stats=cat_stats,
    )


async def test_setup_entry_lists_all_sensor_states(hass, setup_integration):
    states = hass.states.async_all("sensor")
    assert len(states) == 10


def test_operating_state_maps_to_option(sample_device, sample_status, sample_cat):
    status = dataclasses.replace(sample_status, operating_state=OperatingState.CLEANING)
    snap = _make_snapshot(sample_device, status, sample_cat)
    s = NeakasaOperatingStateSensor(_coord_with(snap), sample_device.iot_id)
    assert s.native_value == "cleaning"
    assert s.unique_id == f"{sample_device.iot_id}_operating_state"
    assert set(s.options) == {
        "idle",
        "cleaning",
        "restoring",
        "leveling",
        "cat_appears",
    }


def test_operating_state_unknown_becomes_none(sample_device, sample_status, sample_cat):
    status = dataclasses.replace(sample_status, operating_state=OperatingState.UNKNOWN)
    snap = _make_snapshot(sample_device, status, sample_cat)
    s = NeakasaOperatingStateSensor(_coord_with(snap), sample_device.iot_id)
    assert s.native_value is None


def test_operating_state_none_without_snapshot(sample_device):
    coord = MagicMock()
    coord.data = NeakasaPayload(devices={})
    coord.last_update_success = True
    s = NeakasaOperatingStateSensor(coord, sample_device.iot_id)
    assert s.native_value is None


def test_sand_percent_native_value(sample_device, sample_status, sample_cat):
    snap = _make_snapshot(sample_device, sample_status, sample_cat)
    s = NeakasaSandPercentSensor(_coord_with(snap), sample_device.iot_id)
    assert s.native_value == sample_status.sand_percent
    assert s.unique_id == f"{sample_device.iot_id}_sand_percent"


def test_sand_percent_returns_none_when_no_snapshot(sample_device):
    coord = MagicMock()
    coord.data = NeakasaPayload(devices={})
    coord.last_update_success = True
    s = NeakasaSandPercentSensor(coord, sample_device.iot_id)
    assert s.native_value is None


def test_visits_today_value(sample_device, sample_status, sample_cat):
    snap = _make_snapshot(sample_device, sample_status, sample_cat)
    s = NeakasaVisitsTodaySensor(_coord_with(snap), sample_device.iot_id)
    assert s.native_value == 2


def test_visits_today_none_without_snapshot(sample_device):
    coord = MagicMock()
    coord.data = NeakasaPayload(devices={})
    coord.last_update_success = True
    s = NeakasaVisitsTodaySensor(coord, sample_device.iot_id)
    assert s.native_value is None


def test_last_visit_value(sample_device, sample_status, sample_cat):
    snap = _make_snapshot(sample_device, sample_status, sample_cat)
    s = NeakasaLastVisitSensor(_coord_with(snap), sample_device.iot_id)
    assert s.native_value == datetime.fromtimestamp(1_700_000_500, tz=UTC)


def test_last_visit_none_when_no_history(sample_device, sample_status, sample_cat):
    snap = _make_snapshot(sample_device, sample_status, sample_cat, last_visit_at=None)
    s = NeakasaLastVisitSensor(_coord_with(snap), sample_device.iot_id)
    assert s.native_value is None


def test_last_visit_none_without_snapshot(sample_device):
    coord = MagicMock()
    coord.data = NeakasaPayload(devices={})
    coord.last_update_success = True
    s = NeakasaLastVisitSensor(coord, sample_device.iot_id)
    assert s.native_value is None


def test_cat_weight_returns_latest_visit_weight(
    sample_device, sample_status, sample_cat
):
    snap = _make_snapshot(
        sample_device,
        sample_status,
        sample_cat,
        cat_stats={
            sample_cat.id: {
                "last_visit_at": 1_700_000_500,
                "last_visit_weight": 4.65,
                "last_visit_weight_unit": "kg",
                "visits_today": 3,
            },
        },
    )
    s = NeakasaCatWeightSensor(_coord_with(snap), sample_device.iot_id, sample_cat.id)
    assert s.native_value == 4.65
    assert s.native_unit_of_measurement == UnitOfMass.KILOGRAMS
    assert s.unique_id.endswith("_weight")


def test_cat_weight_uses_pounds_from_latest_record(
    sample_device, sample_status, sample_cat
):
    snap = _make_snapshot(
        sample_device,
        sample_status,
        sample_cat,
        cat_stats={
            sample_cat.id: {
                "last_visit_at": 1_700_000_500,
                "last_visit_weight": 10.56,
                "last_visit_weight_unit": "lbs",
                "visits_today": 3,
            },
        },
    )
    s = NeakasaCatWeightSensor(_coord_with(snap), sample_device.iot_id, sample_cat.id)
    assert s.native_value == 10.56
    assert s.native_unit_of_measurement == UnitOfMass.POUNDS


def test_cat_weight_falls_back_to_profile_unit(
    sample_device, sample_status, sample_cat
):
    cat = dataclasses.replace(sample_cat, unit="lb")
    snap = _make_snapshot(
        sample_device,
        sample_status,
        cat,
        cat_stats={
            cat.id: {
                "last_visit_at": 1_700_000_500,
                "last_visit_weight": 10.56,
                "last_visit_weight_unit": "",
                "visits_today": 3,
            },
        },
    )
    s = NeakasaCatWeightSensor(_coord_with(snap), sample_device.iot_id, cat.id)
    assert s.native_unit_of_measurement == UnitOfMass.POUNDS


def test_cat_weight_none_without_payload(sample_device, sample_cat):
    coord = MagicMock()
    coord.data = None
    coord.last_update_success = True
    s = NeakasaCatWeightSensor(coord, sample_device.iot_id, sample_cat.id)
    assert s.native_value is None


def test_cat_weight_none_when_device_missing(sample_device, sample_cat):
    coord = MagicMock()
    coord.data = NeakasaPayload(devices={})
    coord.last_update_success = True
    s = NeakasaCatWeightSensor(coord, sample_device.iot_id, sample_cat.id)
    assert s.native_value is None


def test_cat_weight_none_when_stats_missing(sample_device, sample_status, sample_cat):
    snap = _make_snapshot(sample_device, sample_status, sample_cat, cat_stats={})
    s = NeakasaCatWeightSensor(_coord_with(snap), sample_device.iot_id, sample_cat.id)
    assert s.native_value is None


def test_cat_last_visit(sample_device, sample_status, sample_cat):
    snap = _make_snapshot(sample_device, sample_status, sample_cat)
    s = NeakasaCatLastVisitSensor(
        _coord_with(snap), sample_device.iot_id, sample_cat.id
    )
    assert s.native_value == datetime.fromtimestamp(1_700_000_500, tz=UTC)


def test_cat_last_visit_none_without_payload(sample_device, sample_cat):
    coord = MagicMock()
    coord.data = None
    coord.last_update_success = True
    s = NeakasaCatLastVisitSensor(coord, sample_device.iot_id, sample_cat.id)
    assert s.native_value is None


def test_cat_last_visit_none_without_device(sample_device, sample_cat):
    coord = MagicMock()
    coord.data = NeakasaPayload(devices={})
    coord.last_update_success = True
    s = NeakasaCatLastVisitSensor(coord, sample_device.iot_id, sample_cat.id)
    assert s.native_value is None


def test_cat_last_visit_none_when_stats_missing(
    sample_device, sample_status, sample_cat
):
    snap = _make_snapshot(sample_device, sample_status, sample_cat, cat_stats={})
    s = NeakasaCatLastVisitSensor(
        _coord_with(snap), sample_device.iot_id, sample_cat.id
    )
    assert s.native_value is None


def test_cat_visits_today(sample_device, sample_status, sample_cat):
    snap = _make_snapshot(sample_device, sample_status, sample_cat)
    s = NeakasaCatVisitsTodaySensor(
        _coord_with(snap), sample_device.iot_id, sample_cat.id
    )
    assert s.native_value == 3


def test_cat_visits_today_none_without_payload(sample_device, sample_cat):
    coord = MagicMock()
    coord.data = None
    coord.last_update_success = True
    s = NeakasaCatVisitsTodaySensor(coord, sample_device.iot_id, sample_cat.id)
    assert s.native_value is None


def test_cat_visits_today_none_when_stats_missing(
    sample_device, sample_status, sample_cat
):
    snap = _make_snapshot(sample_device, sample_status, sample_cat, cat_stats={})
    s = NeakasaCatVisitsTodaySensor(
        _coord_with(snap), sample_device.iot_id, sample_cat.id
    )
    assert s.native_value is None


def test_cat_visits_today_none_without_device(sample_device, sample_cat):
    coord = MagicMock()
    coord.data = NeakasaPayload(devices={})
    coord.last_update_success = True
    s = NeakasaCatVisitsTodaySensor(coord, sample_device.iot_id, sample_cat.id)
    assert s.native_value is None


def test_time_in_box_sums_only_this_cats_completed_visits(
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

    assert snap.cat_stats[sample_cat.id]["time_in_box_today_seconds"] == 75
    assert snap.cat_stats[other_cat.id]["time_in_box_today_seconds"] == 45


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
def test_time_in_box_clips_at_local_midnight_and_ignores_invalid_or_future_durations(
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

    assert snap.cat_stats[sample_cat.id]["time_in_box_today_seconds"] == expected


def test_time_in_box_is_zero_without_records(sample_device, sample_status, sample_cat):
    snap = _build_snapshot(sample_device, sample_status, [sample_cat], [])
    assert snap.cat_stats[sample_cat.id]["time_in_box_today_seconds"] == 0


def test_time_in_box_resets_on_next_local_day(
    local_day, sample_device, sample_status, sample_cat, sample_record, freezer
):
    visit = replace(sample_record, start_time=local_day + 60, end_time=local_day + 105)
    before = _build_snapshot(sample_device, sample_status, [sample_cat], [visit])
    freezer.move_to(datetime(2026, 10, 25, 12, tzinfo=UTC))
    after = _build_snapshot(sample_device, sample_status, [sample_cat], [visit])

    assert before.cat_stats[sample_cat.id]["time_in_box_today_seconds"] == 45
    assert after.cat_stats[sample_cat.id]["time_in_box_today_seconds"] == 0


@pytest.mark.parametrize(
    "day",
    [datetime(2026, 3, 29, 12, tzinfo=UTC), datetime(2026, 10, 25, 12, tzinfo=UTC)],
)
def test_time_in_box_uses_local_midnight_on_daylight_saving_transition(
    day, local_day, sample_device, sample_status, sample_cat, sample_record, freezer
):
    freezer.move_to(day)
    midnight = int(dt_util.start_of_local_day().timestamp())
    visit = replace(sample_record, start_time=midnight - 50, end_time=midnight + 20)
    snap = _build_snapshot(sample_device, sample_status, [sample_cat], [visit])

    assert snap.cat_stats[sample_cat.id]["time_in_box_today_seconds"] == 20


def test_time_in_box_sensor_contract(
    local_day, sample_device, sample_status, sample_cat, sample_record
):
    visit = replace(sample_record, start_time=local_day + 60, end_time=local_day + 105)
    snap = _build_snapshot(sample_device, sample_status, [sample_cat], [visit])
    coordinator = MagicMock()
    coordinator.data = NeakasaPayload(devices={sample_device.iot_id: snap})
    sensor = NeakasaCatTimeInBoxTodaySensor(
        coordinator, sample_device.iot_id, sample_cat.id
    )

    assert sensor.native_value == 45
    assert (
        sensor.unique_id
        == f"{sample_device.iot_id}_cat_{sample_cat.id}_time_in_box_today"
    )
    assert sensor.translation_key == "cat_time_in_box_today"
    assert sensor.native_unit_of_measurement == UnitOfTime.SECONDS
    assert sensor.suggested_unit_of_measurement == UnitOfTime.MINUTES
    assert sensor.device_class == SensorDeviceClass.DURATION
    assert sensor.state_class == SensorStateClass.TOTAL_INCREASING


@pytest.mark.parametrize("missing", ["payload", "device", "stats"])
def test_time_in_box_sensor_returns_none_when_data_missing(
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
    sensor = NeakasaCatTimeInBoxTodaySensor(
        coordinator, sample_device.iot_id, sample_cat.id
    )

    assert sensor.native_value is None


async def test_time_in_box_sensor_registered_with_translated_name(
    hass, setup_integration, sample_device, sample_cat
):
    registry = er.async_get(hass)
    entity_id = registry.async_get_entity_id(
        "sensor",
        "neakasa_litterbox",
        f"{sample_device.iot_id}_cat_{sample_cat.id}_time_in_box_today",
    )
    assert entity_id is not None
    state = hass.states.get(entity_id)
    assert state is not None
    assert float(state.state) == 0
    assert state.attributes["friendly_name"] == f"{sample_cat.name} Time in box today"
    assert state.attributes["device_class"] == "duration"
    assert state.attributes["state_class"] == "total_increasing"
    assert state.attributes["unit_of_measurement"] == "min"
