# Umrechnungsfaktor
inch = 2.54

print(f"{'Inch':>4}{'cm':>12}")

for i in range(15, 41, 5):
    print(f"{i:>7.1f}{i * inch:>7.1f}")
