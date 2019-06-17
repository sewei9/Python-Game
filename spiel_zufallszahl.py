# Modul random importieren
import random
# Zufallsgenerator intialisieren
random.seed()

#Zufallswerte und Berechnung
a = random.randint(1,10)
b = random.randint(1,10)
c = a + b
print("Die Aufgabe:", a, "+", b)

# Eingabe
print("Bitte die Zahl eingeben:")
z = input()
zahl = int(z)

# Ausgabe
print("Ihre EIngabe ist:", z)
print("Das Ergebnis:", c)


