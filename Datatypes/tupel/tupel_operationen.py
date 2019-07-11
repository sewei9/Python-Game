# Tupel mit und ohne Klammern
z1 = (3, 6, -8, 5.5)
print("Tupel 1:", z1)

z2 = 6, 8, -3
print("Tupel 2:", z2)

# Mehrdimensionales Tupel, unterschiedliche Objekte
x = (("Paris", "Fr", 3500000), ["Rom", "It", 4200000])
print("mehrdim. Tupel", x)

# Ersetzen
print("Es soll versucht werden ein Element innerhalb des Tupels zu ersetzen")
print("try: x[0][0] = Lyon except: print(Fehler)")
try:
    x[0][0] = "Lyon"        # Nicht erlaubt weil Tupel!
except:
    print("Fehler")

x[1][0] = "Pisa"            # Erlaubt, weil [1] eine Liste ist
print("Listenelement Rom durch Pisa ersetzt:", x[1])

# Tupel bei for-Schleife
for i in 4, 5, 12:
    print("i:", i)

# Zuweisung mit Tupel
x, y = 2, 18
print("x:", x, "y:", y)
