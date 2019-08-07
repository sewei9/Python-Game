# Definition einer Enumeration mit ganzen Zahlen. Aufzaehlungvon Konstanten
import enum


class Farbe(enum.IntEnum):
    rot = 5
    gelb = 2
    blau = 4


# Vergleich
x = 4
if x == Farbe.gelb:
    print("Das ist gelb")
else:
    print("Es ist eine andere Farbe")
print()


# Alle Elemente
for f in Farbe:
    print(f, repr(f))
print()


# Verschiedene Ausgaben und Berechnungen
print(Farbe.gelb)
print(Farbe.gelb * 1)
print(Farbe.gelb * 10)
