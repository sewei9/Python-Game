def steuer(x):
    if x > 2500:
        s = x * 0.22
        print("Gehalt:", x ,"Steuern", s)
    else:
        s = x * 0.18
        print("Gehalt", x ,"Steuern", s)
        
#Hauptprogramm
steuer(1800)
steuer(2200)
steuer(2500)
steuer(2900)