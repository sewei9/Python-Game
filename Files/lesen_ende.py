import sys

# Zugriffsversuch
try:
    d = open("lesen.txt")
except:
    print("Dateizugriff nicht möglich")
    sys.exit(0)

# Lesen, Ausgabe und SUmmierung aller Zeilen
summe = 0
zeile = d.readline()
while zeile:
    summe += float(zeile)
    print(zeile, end="")
    zeile = d.readline()

# Ausgabe der Summe
print("Summe:", summe)

# Schliessen der Datei
d.close()
