class DiaryStatistics:
    """Päeviku statistika arvutamise klass (analüüs)."""

    @staticmethod
    def print_statistics(diary):
        """Prindib sissekannete koguarvu ja keskmise pikkuse."""
        count = len(diary.entries)
        if count == 0:
            print("Päevik on tühi. Statistika puudub.")
            return

        # Arvutame kõigi sissekannete tähemärkide summa
        total_chars = sum(len(entry) for entry in diary.entries)
        avg_chars = total_chars / count

        print("--- Päeviku statistika ---")
        print(f"Sissekannete arv: {count}")
        print(f"Keskmine tähemärkide arv: {avg_chars:.1f}")
        print("--------------------------")

    @staticmethod
    def get_entry_count(diary):
        """Tagastab sissekannete arvu."""
        return len(diary.entries)

    @staticmethod
    def get_average_length(diary):
        """Tagastab keskmise sissekande pikkuse."""
        count = len(diary.entries)
        if count == 0:
            return 0
        total_chars = sum(len(entry) for entry in diary.entries)
        return total_chars / count
