#Eingabe Bruttogehalt
print("Bitte geben Sie ihr Bruttogehalt in Euro an:")
z = float(input())
steuern = z * 0.22
bg = z * 0.18

# Eingabe in Zahl umwandeln
zahl = int(z)

# Berechnung des Bruttogehalts
if zahl > 2500:
    print ("Ihre Steuerabgaben belaufen sich auf:", steuern)
else:
    print("Ihre Steuerabgaben belaufen sich auf:", bg)


#Ausgabe Bruttogehalt
#print("Ihre Steuerabgaben belaufen sich auf:", steuern)
#print("Ihr Nettogehalt beträgt:", bg)
