# Definition der Klasse LKW
class LKW(Fahrzeug):
    def __init__(self, bez, ge, la):
        Fahrzeug.__init__(self, bez, ge)
        self.ladung = la

    def __str_(self):
        return Fahrzeug.__str__(self) + " " \
            + str(self.ladung) + " Tonnen Ladung"

    def beladen(self, wert):
        self.ladung += wert

    def entladen(self, wert):
        self.ladung -= wert
