## Neakasa Litterbox v1.5.0b1 — Upstream-based activity and leveling preview

### What's new
- Rebased feature development on the upstream v1.5.0 code, including merged PRs #106 (record deduplication) and #107 (native per-cat time in box today).
- Restore the `Recent activity` sensor and its existing structured `events` attributes for dashboard compatibility.
- Include cat visits, cleaning cycles and observed leveling completions in the activity timeline.
- Retain measured leveling durations and completed events across Home Assistant restarts.
- Prune expired leveling events and orphaned durations from restored state.
- Guard against delayed cloud status replay creating a duplicate leveling completion shortly after a confirmed cycle.

### Validation
- 208 Python tests passed; 97.16% code coverage (prior to beta version bump).
- Ruff, Mypy, HACS, Hassfest and version checks passed.
- The integration retains compatibility with the existing stable Neakasa M1 card; no card update is required.

### Important compatibility note
- The upstream `*_time_in_box_today` entity remains available, while the legacy `*_stay_today` entity is also preserved with its original unique ID and seconds unit for existing dashboards.
- Existing Neakasa M1 cards and dashboard YAML need no changes or updates.
- The `*_recent_activity` entity retains its original unique ID and `events` schema.

### Known limitations
- A leveling cycle must be observed to derive its duration; fully missed cycles cannot be reconstructed.
- The 120-second post-completion guard is a provisional mitigation for stale cloud observations.
- The SDK does not reliably distinguish manual from automatic leveling.
- Event-platform architecture and long-term public history access remain under upstream discussion in issue #108.
- Beta requires real-device validation and should not be promoted to stable solely based on CI.

### Installation and test plan
1. Back up the existing v1.4.5 integration configuration, and note the last activity event.
2. Install v1.5.0b1 through the integration's HACS beta channel and restart Home Assistant.
3. Keep the currently installed Neakasa M1 card and its YAML unchanged.
4. Verify cat visits, cleaning entries, leveling duration, recent activity after reload, and retention across a Home Assistant restart.
5. Report any duplicate leveling events or missing entries with MQTT/cloud timing details.
