#Initialisierung while-loop
fehler = 1

#Umrechnungsfaktor
inch = 2.54

#Schleife bei falscher Eingabe
while fehler == 1:
    #Eingabe inch-Wert
    print("Bitte geben Sie den inch-Wert ein")
    xi = input()
    #xi = float(input())

    #Versuch der Umrechnung
    try:
        xi = float(xi)
        fehler = 0
        #print(xi, "Inch sind", xcm, "cm")
    
    #Fehler bei Umrechnung
    except:
        print("Ihre Eingabe entspricht keiner Zahl. Bitte erneut eingeben")
    
    #Umrechnung, Ausgabe
    xcm = xi * inch
    print(xi, "Inch sind", xcm, "cm")