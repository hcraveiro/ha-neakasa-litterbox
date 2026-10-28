"""Daily visit-duration sensor for a cat on a Neakasa litter box."""

from __future__ import annotations

from typing import TYPE_CHECKING

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.const import UnitOfTime

from ..entity import NeakasaCatEntity

if TYPE_CHECKING:
    from ..data import NeakasaPayload


class NeakasaCatStayTodaySensor(NeakasaCatEntity, SensorEntity):
    """Total recorded visit duration for this cat during the local day."""

    _attr_translation_key = "cat_stay_today"
    _attr_icon = "mdi:timer-outline"
    _attr_native_unit_of_measurement = UnitOfTime.SECONDS
    _attr_device_class = SensorDeviceClass.DURATION
    _attr_state_class = SensorStateClass.TOTAL_INCREASING

    @property
    def unique_id(self) -> str:
        """Return the stable unique id."""
        return f"{self.iot_id}_cat_{self.cat_id}_stay_today"

    @property
    def native_value(self) -> int | None:
        """Return today's completed visit duration in seconds."""
        payload: NeakasaPayload | None = self.coordinator.data
        if payload is None:
            return None
        device = payload.devices.get(self.iot_id)
        if device is None:
            return None
        stats = device.cat_stats.get(self.cat_id)
        return None if stats is None else stats["stay_today_seconds"]
