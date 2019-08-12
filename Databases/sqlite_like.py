import sqlite3

# Verbindung, Curosor
connection = sqlite3.connect("firma.db")
cursor = connection.cursor()

# SQL- Abfragen

# Beliebig viele beliebige Zeichen
sql = "SELECT * FROM personen WHERE name LIKE 'm%'"     #Looking for person where the first letter is m
cursor.execute(sql)
for dsatz in cursor:
    print(dsatz[0], dsatz[1])
print()

# Beinhaltet...
sql = "SELECT * FROM personen WHERE name LIKE '%i%'"    # Wildcardcharacter %?%
cursor.execute(sql)
for dsatz in cursor:
    print(dsatz[0], dsatz[1])
print()

# Einzelne beliebe Zeichen
sql = "SELECT * FROM personen WHERE name LIKE 'M__er'"
cursor.execute(sql)
for dsatz in cursor:
    print(dsatz[0], dsatz[1])

# Verbindung beenden
connection.close()
