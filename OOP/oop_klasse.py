# Definition der Klasse Fahrzeug
class Fahrzeug:
    geschwindigkeit = 0                 # Eigenschaft
    def beschleunigung(self, wert):     # Methode
        self.geschwindigkeit += wert
    def ausgabe(self):                   # Methode
        print("Geschwindigkeit:", self.geschwindigkeit)


# objekte der Klasse Fahrzeug erzeugen
opel = Fahrzeug()
volvo = Fahrzeug()

# Objektmethoden
volvo.ausgabe()
volvo.beschleunigung(20)
volvo.ausgabe()

# Objekt betrachten
opel.ausgabe()


