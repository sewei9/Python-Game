def steuer(x):
    if x > 2500:
        s = x * 0.22
        print("Gehalt:", x ,"Steuern", s)
    else:
        s = x * 0.18
        print("Gehalt", x ,"Steuern", s)
    return s

print("Bruttobetrag: 1800, Steuerbetrag", steuer(1800))
print("Bruttobetrag: 2200, Steuerbetrag", steuer(2200))
print("Bruttobetrag: 2500, Steuerbetrag", steuer(2500))
print("Bruttobetrag: 2900, Steuerbetrag", steuer(2900))
