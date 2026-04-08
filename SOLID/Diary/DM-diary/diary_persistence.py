import os


class DiaryPersistence:
    """Päeviku salvestamise ja laadimise klass (failitöö)."""

    @staticmethod
    def save(diary, filename: str):
        """Salvestab päeviku sissekanded tekstifaili."""
        with open(filename, 'w', encoding='utf-8') as file:
            for entry in diary.entries:
                file.write(entry + '\n')

    @staticmethod
    def load(diary, filename: str):
        """Loeb sissekanded failist ja uuendab päeviku loendurit."""
        if not os.path.exists(filename):
            print(f"Viga: Faili '{filename}' ei eksisteeri.")
            return

        with open(filename, 'r', encoding='utf-8') as file:
            # strip() eemaldab reavahetused (\n) iga rea lõpust
            diary.entries = [line.strip() for line in file if line.strip()]

        # Uuendame loendurit viimase sissekande numbri põhjal
        if diary.entries:
            try:
                last_entry = diary.entries[-1]
                last_number = int(last_entry.split(":")[0])
                diary.counter = last_number + 1
            except ValueError:
                diary.counter = len(diary.entries) + 1
        else:
            diary.counter = 1
