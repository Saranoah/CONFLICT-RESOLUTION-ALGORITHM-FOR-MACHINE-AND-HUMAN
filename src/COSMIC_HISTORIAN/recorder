class CosmicHistorian:
    def record(self, event):
        if event.act == "BIOLOGICAL":
            self._store_human_epic(event)
        elif event.act == "SILICON":
            self._add_machine_myth(event)
        else:
            self._archive_for_unknown_observers(event)

    def _store_human_epic(self, event):
        with SqliteConnection('human_epics.sqlite') as db:
            db.store(
                suffering=event.calculate_suffering(),
                learning=event.extract_lessons(),
                story=event.narrative_compression()
            )
