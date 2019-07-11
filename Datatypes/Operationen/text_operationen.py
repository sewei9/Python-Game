# Beispielsequenz, hier Zeichenkette
tname = "Robinson Crusoe"
print("Text:", tname)

# Anzahl Elemente
lg = len(tname)
print("Anzahl Elemente:", lg)

# Teilbereiche, Elemente
ts = tname[5:8]  # Slice von ...bis
print("[5:8]:", ts)

ts = tname[:8]  # Slice bis
print("[:8]:", ts)

ts = tname[9:]  # Slice von
print("[9:]:", ts)

ts = tname[9]
print("[9]:", ts)

ts = tname[9:-3]
print("[9:-3]:", ts)

# Elemente einzeln
#
for zeichen in tname[5:8]:
    print(zeichen)
