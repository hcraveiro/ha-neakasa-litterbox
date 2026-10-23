## Neakasa Litterbox v1.4.4b4 — Confirmed leveling duration

### Improvements
- Detect leveling completion after a sustained MQTT `leveling` → `idle` transition, rejecting transient state glitches shorter than 15 seconds.
- Measure the actual observed duration and publish `duration_seconds` in the native `recent_activity.events` sensor.
- Persist completion timestamps and durations in Home Assistant storage across restarts.
- Preserve activity history and measured times through cloud polling refreshes.
- Continue exposing cloud cleaning completion times and per-cat daily durations.

### Validation
The preceding v1.4.4b3 live test observed `leveling` from 07:51:42 to 07:52:22 (approximately 40 seconds), followed by a cat visit. The v1.4.4b4 regression tests reproduce this case and verify that a short idle glitch does not create a false completion.

### Limitations
- Previously completed leveling events are not imported retroactively.
- Leveling must be observed on the MQTT status stream from start to finish to be recorded.
- Manual versus automatic leveling cannot yet be distinguished reliably using the exposed SDK status; consumers should not rely on this classification.
- Duration is measured from received status transitions and may differ slightly from physical operation time.

### Installation
Update the Neakasa Litterbox integration in HACS to v1.4.4b4, restart Home Assistant, and perform one manual leveling test. The Neakasa M1 Card v1.2.1 already supports showing `Manual leveling completed in X s` when a nonzero duration is provided.

Keep the old YAML logging package until the live event is verified.
