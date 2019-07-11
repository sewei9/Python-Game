# 1: Mehrfache Zuweisung
x, y, z = 3, 5.2, "hallo"
print("Mehrfache Zuweisung:", x, y, z)

# 2: Auswirkungen erst danach
a = 12
b = 15
c = 22
a, b, c = c, a, a+b
print("Auswirkungen:", a, b, c)

# 3: Verpacken eines Tupels
p = 3, 4
print("Verpackt:", p)

# 4: Entpacken eines Tupels
m, n = p
print("Entpacken eines Tupels:", "m:", m, "n:", n)

# 5: falsche Zuweisung eines Tupels
try:
    s, t = 3, 4, 12
    print(s, t)
except:
    print("Fehler")

# 6: Rest in Liste
print()
x, *y, z = 3, 5.2, "hallo", 7.3, 2.9
print(x)
print(y)
print(z)
# kein Rest , Liste leer
print()
x, *y, z = 3, 5.2
print(x)
print(y)
print(z)