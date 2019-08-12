import random, time
# Hauptprogramm
s = Spiel()
s.messen(True)
s.spielen()
s.messen(False)
print s

class Spiel:
    # ....

    def messen(self, start):
        # Zeitmessung
        if start:
            self.startzeit =time.time()
        else:
            endzeit = time.time()
            selt.zeit = endzeit - self.startzeit
    
    def __str__(self):
        # Ergebnis
        datum = time.strftime("%d.%m.%Y")
        uhrzeit = time.strftime(%H:%M:%S")
        ausgabe = f"Richtig: {self.richtig:d} von " \
                    f"{self.anzahl:d} in {self.zeit:.2f}" \
                        f" Sekunden\nam {datum} um {uhrzeit}"
        return ausgabe