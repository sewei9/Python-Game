# Erste function
def eingabe():
    global x
    x = input("Zahl:")
    x = float(x)

# Zweite function
def ausgabe():
    print(x*2)

# Main program
eingabe()
ausgabe()