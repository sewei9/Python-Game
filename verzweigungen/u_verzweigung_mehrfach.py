#Eingabe Bruttogehalt
print("Bitte geben Sie ihr Bruttogehalt in Euro an:")
z = float(input())
steuern1 = z * 0.26
steuern2 = z * 0.22
steuern3 = z * 0.18

# Eingabe in Zahl umwandeln
zahl = int(z)

# Berechnung des Bruttogehalts
if zahl > 4000:
    print ("Ihre Steuerabgaben belaufen sich auf:", steuern1)
elif zahl >= 2500:
    print ("Ihre Steuerabgaben belaufen sich auf:", steuern2)
else:
    print("Ihre Steuerabgaben belaufen sich auf:", steuern3)


#Ausgabe Bruttogehalt
#print("Ihre Steuerabgaben belaufen sich auf:", steuern)
#print("Ihr Nettogehalt beträgt:", bg)
