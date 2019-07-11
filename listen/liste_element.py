# Originalliste
fr = ["Paris", "Lyon", "Marseille", "Bordeaux"]
print("Original:", fr)

# Ersetzen eines Elements durch ein Element
fr[2] = "Lens"
print("Element ersetzt:", fr)

# Ersetzen eines Teilbereichs durch eine Liste
fr[1:2]= ["Nacy", "Metz"]
print("Teil ersetzt:", fr)

# Entnehmen eines Teilbereiches
del fr[3:]
print("Teil entnommen:", fr)

# Ersetzen eines Elements durch eine Liste
fr[0] = ["Paris-Nord", "Paris-Sued"]
print("Element durch Liste ersetzt:", fr)