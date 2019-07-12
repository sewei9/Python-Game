# Originalliste
fr = ["Paris", "Lyon", "Marseille"]
print("Original:", fr)

# Einsetzen eines Elements
fr.insert(0,"Nantes")
print("Neu:", fr)

# Sortieren der Elemente
fr.sort()
print("Nach sortieren:", fr)

# Umdrehen der Liste
fr.reverse()
print("Liste umgedreht:", fr)

# Entfernen es Elements
fr.remove("Nantes")
print("Nach Entfernen:", fr)

# Ein Element am Ende hinzufuegen
fr.append("Paris")
print("Nach hinzufuegen:", fr)

# Anzahl bestimmer Elemente
print("Anzahl Elemente Paris:",fr.count("Paris"))

# Suchen bestimmter Elemente
print("Index von Paris:", fr.index("Paris"))