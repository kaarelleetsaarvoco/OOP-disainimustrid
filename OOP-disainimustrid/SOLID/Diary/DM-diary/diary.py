class Diary:
    """Päeviku klass sissekannete haldamiseks (andmete haldus)."""

    def __init__(self):
        """Konstruktor loob tühja nimekirja ja algseadistab loenduri."""
        self.entries = []
        self.counter = 1

    def add_entry(self, text: str):
        """Lisab uue sissekande koos järjekorranumbriga."""
        entry = f"{self.counter}: {text}"
        self.entries.append(entry)
        self.counter += 1

    def del_entry(self, index: int):
        """Kustutab sissekande listi indeksi järgi (0-põhine)."""
        if 0 <= index < len(self.entries):
            self.entries.pop(index)
        else:
            print(f"Viga: Sissekannet indeksiga {index} ei leitud.")

    def __str__(self):
        """Tagastab kõik sissekanded reavahetustega eraldatult."""
        if not self.entries:
            return "Päevik on tühi."
        return "\n".join(self.entries)
