# Function zur Berechnung einzelner Werte
def quadrat(x):
    return x * x

# FUnction zur Berechnung einzelner WErte


def hochdrei(x):
    return x * x * x

# Function zur Ausgabe von Funktionswerten


def ausgabe(unten, oben, schritt, f):
    for x in range(unten, oben, schritt):
        print(x, f(x))
    print()


# Aufruf, Functionname ist Parameter
ausgabe(2, 11, 2, quadrat)
ausgabe(1, 6, 1, hochdrei)
# S.189