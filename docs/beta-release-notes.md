## Neakasa Litterbox v1.4.5b1 — Leveling completion across MQTT and polling

### Fix
- Track leveling start and completion consistently across MQTT status updates and cloud polling.
- Record completed leveling cycles even when their starting and ending transitions arrive through different update paths.
- Keep the minimum 15-second confirmation threshold to reject short contradictory state spikes.
- Persist measured leveling durations and timestamps in native recent activity.

### Regression coverage
- Test a 98-second leveling cycle with both transitions from cloud polling.
- Test mixed MQTT/poll transitions in both directions.
- Test duplicate same-state observations do not generate duplicate completions.

### Installation and validation
Update to v1.4.5b1 through HACS (enable pre-releases), restart Home Assistant, trigger a manual leveling cycle, and check that a leveling event appears in the Recent Activity sensor after returning to idle.

### Known limitations
- A leveling operation that begins and ends entirely between observations cannot be reconstructed.
- Manual versus automatic leveling cannot be reliably distinguished by the SDK.
