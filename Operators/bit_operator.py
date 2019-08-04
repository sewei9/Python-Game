# Nur 1 Bit gesetzt
bit0 = 1  # 0000 0001
bit3 = 8  # 0000 1000
print(bin(bit0), bin(bit3))

# Bitweises AND
a = 5  # 0000 0101
erg = a & bit0  # 0000 0001
if erg:
    print(a, "ist ungerade")

# Bitweises OR
erg = 0
erg = erg | bit0  # | Dient zur bitweisen Oder-Verknüpfung zweier Zahlen
erg = erg | bit3
print("Bits nacheinander gesetzt:", erg, bin(erg))

# Bitweises Exclusive-OR
a = 21  # 0000 0000
b = 19  # 0000 0001
erg = a ^ b  # 0000 1001
print("Ungleiche Bits:", erg, bin(erg))

# Bitweise Inversion, aus x wird -(x+1)
a = 11  # 0000 1011
erg = ~a  # 1111 0100
print("Bitweise Inversion:", erg, bin(erg))

# Bitweise schieben
a = 11  # 0000 1011
erg = a >> 1  # 0000 0101
print("Um 1 nach rechts geschoben:", erg, bin(erg))
erg = a << 2  # 0010 1100
print("Um 2 nach links geschoben:", erg, bin(erg))
