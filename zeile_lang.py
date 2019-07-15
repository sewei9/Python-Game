print("Umrechnung von Celsius in Fahrenheit")
# Trennung einer Zeichenkette
print("Bitte geben Sie ein"
        " Temperatur in Celsius ein: ")
TemperaturInCelsius = float(input())

# Trennung eines Ausdrucks
TemperaturInFahrenheit = TemperaturInCelsius \
                        * 9 / 5 + 32

# Trennung nach einem Komma
print(TemperaturInCelsius, "Grad in Celsius entsprechen",
    TemperaturInFahrenheit, "Grad in Fahrenheit")