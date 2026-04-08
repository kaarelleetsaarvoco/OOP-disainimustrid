import os

class Diary:
    """Päeviku klass sissekannete haldamiseks."""

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
        """Kustutab sissekande listi indeksi järgi (0-põhine). Kui indeks on vigane, ei tee midagi."""
        if 0 <= index < len(self.entries):
            self.entries.pop(index)
        else:
            print(f"Viga: Sissekannet indeksiga {index} ei leitud.")

    def save(self, filename: str):
        """Salvestab kõik sissekanded tekstifaili."""
        with open(filename, 'w', encoding='utf-8') as file:
            for entry in self.entries:
                file.write(entry + '\n')

    def load(self, filename: str):
        """Loeb sissekanded failist ja uuendab loendurit."""
        if not os.path.exists(filename):
            print(f"Viga: Faili '{filename}' ei eksisteeri.")
            return

        with open(filename, 'r', encoding='utf-8') as file:
            # strip() eemaldab reavahetused (\n) iga rea lõpust
            self.entries = [line.strip() for line in file if line.strip()]

        # Uuendame loendurit viimase sissekande numbri põhjal, et uued 
        # sissekanded jätkaksid õigest numbrist.
        if self.entries:
            try:
                last_entry = self.entries[-1]
                last_number = int(last_entry.split(":")[0])
                self.counter = last_number + 1
            except ValueError:
                self.counter = len(self.entries) + 1
        else:
            self.counter = 1

    def print_statistics(self):
        """Prindib sissekannete koguarvu ja keskmise pikkuse."""
        count = len(self.entries)
        if count == 0:
            print("Päevik on tühi. Statistika puudub.")
            return

        # Arvutame kõigi sissekannete tähemärkide summa
        total_chars = sum(len(entry) for entry in self.entries)
        avg_chars = total_chars / count

        print("--- Päeviku statistika ---")
        print(f"Sissekannete arv: {count}")
        print(f"Keskmine tähemärkide arv: {avg_chars:.1f}")
        print("--------------------------")

    def __str__(self):
        """Tagastab kõik sissekanded reavahetustega eraldatult."""
        if not self.entries:
            return "Päevik on tühi."
        return "\n".join(self.entries)


# testimiseks
if __name__ == '__main__':
    d = Diary()

    #lisab kaks sissekannet
    d.add_entry("Täna oli ilus ilm ja me lähme sõpradega kiikuma.")
    d.add_entry("Õppisin programmeerimist disaini mustrite tunnis.")
    
    # Prindib päeviku sisu
    print("Päeviku sisu:")
    print(d)
    print()
    
    d.save("diary.txt")
    d.print_statistics()
    
    #testib päeviku sissekannete kustutamist
    d.del_entry(0)
    print("\nPäeviku sisu pärast kustutamist:")
    print(d)
    print()
    d.save("diary.txt")