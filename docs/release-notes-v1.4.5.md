# Neakasa Litterbox v1.4.5

## Fixes
- Reconcile leveling start and completion transitions across MQTT push and cloud polling.
- Record confirmed leveling completions in native Recent Activity, even when start and finish arrive from different sources.
- Preserve measured leveling durations and completed events across Home Assistant restarts.
- Retain the 15-second minimum confirmation threshold to avoid transient false-positive completions.

## Validation
- Automated regression tests cover MQTT-to-poll, poll-to-MQTT and coordinator polling transitions.
- Ruff, Mypy, Pytest, Hassfest and HACS validation are required on the release PR.
- A manual leveling cycle was verified on v1.4.5b1 on October 23, 2026: 39 seconds measured, one Recent Activity entry, and correct return to idle.

## Notes
- An operation whose start or end was completely missed cannot be reconstructed.
- Cloud polling can introduce delay into the measured duration.
- The SDK does not reliably distinguish manual from automatic leveling.

## Installation
Update Neakasa Litterbox in HACS to v1.4.5 and restart Home Assistant.
