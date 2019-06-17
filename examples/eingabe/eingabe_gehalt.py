#Eingabe Bruttogehalt
print("Bitte geben Sie ihr Bruttogehalt in Euro an:")
xgh = float(input())

# Eingabe in Zahl umwandeln
zahl = int(xgh)

# Berechnung des Bruttogehalts
steuern = xgh * 0.18
bg = xgh - xgh * 0.18

#Ausgabe Bruttogehalt
print("Ihre Steuerabgaben belaufen sich auf:", steuern)
print("Ihr Nettogehalt beträgt:", bg)

