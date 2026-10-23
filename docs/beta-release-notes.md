## Neakasa Litterbox v1.4.5b1 — Reliable leveling completion

### Fixes
- Reconcile leveling transitions observed through either MQTT or cloud polling.
- Share leveling start tracking across both sources, so mixed-source operations can be recorded.
- Record the observed duration and completion time for confirmed leveling operations.
- Preserve the existing 15-second minimum to reject transient state glitches.
- Keep completed leveling events and durations persisted across Home Assistant restarts.

### Regression coverage
- Leveling starts via cloud polling and ends via MQTT.
- Leveling starts via MQTT and ends via cloud polling.
- Cloud polling delivers the state transition to the common observer.
- Existing MQTT-only leveling duration and transient-state tests remain in place.

### Known limitations
- A leveling operation must have its start and finish observed by the integration; fully missed operations cannot be reconstructed.
- Completion duration is measured between observed transitions and may include delays introduced by cloud polling.
- The SDK does not reliably distinguish manual from automatic leveling.

### Installation
Update to v1.4.5b1 from HACS beta releases and restart Home Assistant. Perform a manual leveling cycle and confirm that it appears in the native Recent Activity sensor after returning to idle.
