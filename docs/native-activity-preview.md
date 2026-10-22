# Native Neakasa activity history (development preview)

This branch adds two types of sensors without replacing any existing entities.

- **Cat Stay today**: one sensor per cat, with today's total recorded time in the litter box, in seconds. It is derived from cloud `CAT_VISIT` records, not from Home Assistant helpers.
- **Recent activity**: one sensor per litter box, with the timestamp of the most recent event as state and an `events` attribute containing at most 30 structured `CAT_VISIT` and `CLEAN_CYCLE` records.

Example `events` payload:

```yaml
events:
  - id: 1234
    type: cat_visit
    cat: Cleo
    cat_id: 567
    timestamp: "2026-10-22T16:26:00+00:00"
    duration_seconds: 46
    weight: 3.9
    weight_unit: kg
  - id: 1235
    type: cleaning
    timestamp: "2026-10-22T16:40:00+00:00"
    duration_seconds: 147
```

These records are retrieved using the integration's existing Neakasa cloud record poll. They survive Home Assistant downtime **only as long as the Neakasa API returns them**. The existing `statistics_lookback_days` option controls the query window.

**Important limitations:**
- The SDK defines `OTHER` records, but their meaning is not known. They are intentionally excluded from the timeline.
- **Manual leveling** has no confirmed cloud record type and is not yet included in the native timeline.
- A card update is needed before the existing Recent Activity card can consume the new sensor's `events` attribute. The old package-based card continues working until then.
- The new numeric stay sensor reports seconds; the Our Cats card must format them as a duration.
- This is an **unreleased draft**, not yet validated with live device data. Keep the current integration and package installed until testing succeeds.

## Validation

The regression tests are located in `tests/test_native_activity.py` and cover duplicate records, cleaning events, daily duration and local-day boundaries. GitHub Actions must run successfully before this draft is promoted to a release.
