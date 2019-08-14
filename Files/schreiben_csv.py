import sys

# Zugriffsversuch
try:
    d = open("daten.csv", "w")
except:
    print("Dateizugriff nicht möglich")
    sys.exit(0)

# Schreiben einer Liste als CSV-Datensatz
li = [42, "maier", 3524.52]
d.write(str(li[0]) + ";" + li[1] + ";"
    + str(li[2]).replace(".",",") + "\n")

# Schreiben einer zweidimensionalen Liste als Datensatztabelle
zli = [[55, "Göclü", 3185.00], [57, "Wäßmann", 2855.20]]
for element in zli:
    d.write(str(element[0]) + ";"
    + element[1] + ";"
    + str(element[2]).replace(".",",") + "\n")
    
# Schliessen der Datei
d.close()