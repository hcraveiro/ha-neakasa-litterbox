## Neakasa Litterbox v1.4.4b1 — Native activity beta

This is an **experimental fork** based on upstream 1.4.3. It adds native per-cat `Stay today` sensors (seconds) and a litter-box `Recent activity` timestamp sensor whose `events` attribute contains structured visits and cleaning cycles from the Neakasa cloud.

**Compatibility:** All existing sensor identifiers remain unchanged. The new sensors are additional. The existing `neakasa_log.yaml` package and custom cards must remain in place until the cards are migrated and live parity verified.

**Known limitation:** Manual leveling does not yet have an identified cloud record representation, so it is not included in the native timeline.

**Installation:** The HACS beta workflow attaches `neakasa_litterbox.zip` to this release. Both fork and upstream use the same integration domain; do not install a duplicate instance. Follow [the beta test plan](https://github.com/hcraveiro/ha-neakasa-litterbox/blob/feat/native-cat-history/docs/beta-test-plan.md) and make a Home Assistant backup first.

**Rollback:** Reinstall the upstream Neakasa Litterbox version and restart HA. Do not delete your existing config entry, package, or entities.
