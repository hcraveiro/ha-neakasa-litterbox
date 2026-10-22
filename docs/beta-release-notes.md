## Neakasa Litterbox v1.4.4b3 — Level-state reliability beta

### Changes since v1.4.4b2
- Avoid immediately polling the cloud after the manual **Level** button is pressed. That poll could replace a genuine MQTT `leveling` update with stale `idle` information.
- Stop treating an instantaneous `leveling` → `idle` transition as **confirmed completion**. Such a transition has been observed only 23 ms after the start while the Android application continued leveling for about one minute.
- Log MQTT and cloud polling operating-state changes separately to diagnose discrepancies.

### Current limitations
- The integration **does not yet reliably know when leveling actually finishes**. This beta deliberately does not create a completion event from an unconfirmed transition.
- Duration and manual-vs-automatic classification remain unconfirmed.
- Past leveling activities cannot be recovered from cloud records.
- The remaining cat activity and cleaning records continue to work normally.

### Live validation
Update v1.4.4b3 through HACS, restart Home Assistant, then manually start leveling. Check whether the `sensor.neakasa_m1_status` remains `leveling` longer than before. Compare MQTT/cloud state diagnostics to the actual Android app status.

**Keep the old logging package while testing.** The old package may also incorrectly label a transient `idle` state as completion.
