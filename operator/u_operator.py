#Eingabe Bruttogehalt
print("Bitte geben Sie ihr Bruttogehalt in Euro an:")
z = float(input())
steuern1 = z * 0.26
steuern2 = z * 0.22
steuern3 = z * 0.22
steuern4 = z * 0.18

# Eingabe in Zahl umwandeln
zahl = int(z)

#Abfrage Verheiratet
print("Sind sie verheiratet?")
v = input()
#Verdienst über 4000
if v == "Ja" and zahl > 4000:
    print("Ihre Steuerabgaben belaufen sich auf:", steuern2)
elif v == "Nein" and zahl > 4000:
        print("Ihre Steuerabgaben belaufen sich auf:", steuern1)
#Verdienst unter 4000       
if v == "Ja" and zahl <= 4000:
    print ("Ihre Steuerabgaben belaufen sich auf:", steuern4)
elif v == "Nein" and  zahl <= 4000:
        print ("Ihre Steuerabgaben belaufen sich auf:", steuern3)


            
    

