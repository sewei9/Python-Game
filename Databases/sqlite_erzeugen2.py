import sqlite3

connection = sqlite3.connect("firma.db")
cursor = connection.cursor()

# Datensatz erzeugen
sql = "INSERT INTO personen VALUES('Maier', " \
    "'Wolfgang', 8339, 3810, '30.06.1959')"
cursor.execute(sql)
connection.commit()

# Verbindung beenden
connection.close()
