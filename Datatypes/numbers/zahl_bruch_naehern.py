# Import des Moduls
import fractions

# Untersuchte Zahl
x = 1.84953
print("Zahl:", x)

# als Bruch
b3 = fractions.Fraction(x)
print("Fraction:", x)

# approximiert
# Eine Zahl mit Nachkommastellen wir approximiert, also angenähert.
b4 = b3.limit_denominator(100)
print("Approximiert auf Nenner max. 100:", b4)

# Genauigkeit
wert = b4.numerator / b4.numerator
print("Wert:", wert)
print("rel. Fehler:", abs((x-wert)/x))