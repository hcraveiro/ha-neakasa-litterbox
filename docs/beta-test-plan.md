# Native activity beta — v1.4.4b1

This is a **testing-only** build of the Neakasa Litterbox integration, based on upstream v1.4.3.

## New entities

- `sensor.<cat>_stay_today` — daily visit duration, **in seconds**, calculated from the Neakasa cloud history.
- `sensor.<litterbox>_recent_activity` — latest activity timestamp with an `events` attribute containing up to 30 cloud visits and clean cycles, including type, cat, weight, duration and timestamps.

Actual entity IDs depend on Home Assistant's entity registry, device names and cat names.

## Safe test plan

1. **Keep the existing `neakasa_log.yaml` package enabled**, so current dashboards and automations continue to work.
2. Make a Home Assistant backup before replacing the integration.
3. Do not add the fork as a second parallel integration: both original and fork use the **same `neakasa_litterbox` domain**. Install the fork as an update/replacement of the existing custom component, not as a separate config entry.
4. Once the beta is published with its HACS ZIP asset, install it using the fork as the source (or manually back up/replace only `custom_components/neakasa_litterbox`). Restart Home Assistant.
5. Check that existing Neakasa entities, buttons and switches still work.
6. Inspect each new stay sensor and the litter box Recent activity sensor's `events` attribute in Developer Tools → States.
7. Compare duration totals and timeline entries against the existing package for at least a day's normal use.
8. Roll back by reinstalling the original integration if you encounter problems.

**Do not remove helpers, automations, or `neakasa_log.yaml` yet.** The Our Cats and Recent Activity frontend cards still use the previous entities and require a separate update to use the new sensor format.

## Known caveats

- Manual leveling events have not been mapped to a confirmed cloud record type and are not in the native activity timeline.
- The cloud history only covers the configured `statistics_lookback_days` interval.
- Each visit that crosses local midnight is credited only for its overlap with the current day.
- The original integration's `hacs.json` has `zip_release: true` with `filename: neakasa_litterbox.zip`. Creating a GitHub release **without attaching that archive** is not sufficient for HACS installation.
- Do not mark this as a stable release until the cloud record data and the card migration have been verified.
