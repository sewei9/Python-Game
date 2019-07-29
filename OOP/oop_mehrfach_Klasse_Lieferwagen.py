# Definition der Klasse Lieferwagen
class Lieferwagen(PKW, LKW):
    def __init__(self, bez, ge, ins, la):
        PKW.__init__(self, bez, ge, ins)
        LKW.__init__(self, bez, ge, ins)

    def __str__(self):
        return PKW.__str__(self) + "\n" \
            + LKW.__str__(self)
