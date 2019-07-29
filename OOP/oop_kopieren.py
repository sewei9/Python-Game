# Modul copy
import copy


# Definition der Klasse Fahrzeug
class Fahrzeug:
    def __init__(self, bez, ge):            # Konstruktormethode
        self.bezeichnung = bez
        self.geschwindigkeit = ge

    def beschleuningen(self, wert):
        self.geschwindigkeit += wert

    def __str__(self):
        return self.bezeichnung + " " \
            + str(self.geschwindigkeit) + "km/h"


# Obekt der KLasse Fahrzeug erzeugen
opel = Fahrzeug("Opel Admiral", 40)

# Kopie eines Objekts erzeugen
zweit_opel = Fahrzeug(opel.bezeichnung, opel.geschwindigkeit)
zweit_opel.beschleuningen(30)

# Tiefe Kopie eines Objekts erzeugen
dritt_opel = copy.deepcopy(opel)
dritt_opel.beschleuningen(35)

# Zweite Referenz auf Objekt erzeugen
viert_opel = opel
viert_opel.beschleuningen(20)

# Kontrollausgaben
print("Original:", opel)
print("Kopie:", zweit_opel)
print("kopie:", dritt_opel)
print("Zweite Referenz auf Original:", viert_opel)

# Identisch
print("2:", opel is zweit_opel)
print("3:", opel is dritt_opel)
print("4:", opel is viert_opel)
