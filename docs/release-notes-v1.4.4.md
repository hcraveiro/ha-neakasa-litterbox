# Neakasa Litterbox v1.4.4

Stable release of the validated v1.4.4b4 integration.

## Improvements
- Record completed leveling operations from sustained MQTT `leveling` → `idle` transitions, filtering short transient state changes.
- Include measured `duration_seconds` and completion timestamps in the native `recent_activity.events` sensor.
- Persist leveling events and durations across Home Assistant restarts.
- Preserve activity history and durations across cloud polling refreshes.
- Provide native cleaning completion records and per-cat daily stay duration sensors.

## Validated on Home Assistant
- Manual leveling completion captured with a measured duration of 39 seconds.
- Manual cleaning recorded as 170 seconds.
- Cat visit recorded with name, weight, and duration; the relevant daily stay total increased by the same duration.
- Automatic cleaning event captured with completion time and duration.

## Known limitations
- MQTT must report the leveling operation from start to finish for the integration to record it.
- The SDK does not reliably distinguish manual from automatic leveling.
- Historical leveling events completed before installation cannot be reconstructed.
- Brief inconsistent operating-state transitions have been observed during cloud/MQTT reconciliation; completed activity records remained correct in the validated tests.

## Installation
Install or update the integration to **v1.4.4** in HACS and restart Home Assistant. Existing entities and dashboard YAML do not need to change.
