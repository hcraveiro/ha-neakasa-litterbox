## Neakasa Litterbox v1.4.4b2 — Native leveling history

This beta extends v1.4.4b1 and restores important activity details required by the Lovelace cards.

### Changes
- Add `completed_at` to cloud activity events so cleaning cycles are displayed at their **completion time**, as in the Neakasa app.
- Capture leveling completions from the live MQTT operating-state transitions.
- Persist recorded leveling times in Home Assistant storage across restarts, and retain them during cloud polling updates.
- Merge leveling events with cloud visits and clean cycles in the `Recent activity` sensor's `events` attribute.
- Keep the v1.4.4b1 per-cat daily stay sensors and other existing entities intact.

### Important limitations
- Leveling events that happened **before installing v1.4.4b2** cannot be recovered from the available cloud history.
- The SDK does not yet distinguish reliably between manually triggered and automatic leveling, so the event is exposed as `leveling`, and the card displays *Leveling completed*.
- A leveling event must be observed through the live MQTT status stream to be recorded. Events during a disconnection may not be captured.

### Installation
This is a prerelease. The release includes `neakasa_litterbox.zip` for HACS. Update your existing integration to this version, restart Home Assistant, and retain the existing entities and configuration entry.

To see the corrected activity texts and leveling icon, also update [Neakasa M1 Card](https://github.com/hcraveiro/neakasa-m1-card) to v1.2.1 or later.

**Do not remove an existing event-logging package until the new timeline has been checked after live leveling tests.**
