# Definition der KLasse Fahrzeug
class Fahrzeug:
    def __init__(self, bez, ge):            # Konstruktormethode
        self.bezeichnung = bez
        self.geschwindigkeit = ge

    def __gt__(self, other):                # 1. Vergleichsmethode
        return self.geschwindigkeit > other.geschwindigkeit

    def __eq__(self, other):                # 2. Vergleichsmethode
        return self.geschwindigkeit == other.geschwindigkeit

    def __sub__(self, other):               # 3. Vergleichsmethode
        return self.geschwindigkeit - other.geschwindigkeit


# Objekte der KLasse Fahrzeuge erzeugen
opel = Fahrzeug("OPel Admiral", 60)
volvo = Fahrzeug("Volvo Amazon", 45)

# Obekte vergleichen
if opel > volvo:
    print("Opel ist schneller als Volvo")
elif opel == volvo:
    print("Beide sind gleich schnell")
else:
    print("Volvo ist schneller")

# Objekte subtrahieren
differenz = opel - volvo
print("Geschwindigkeitsdifferenz:", differenz, "km/h")
