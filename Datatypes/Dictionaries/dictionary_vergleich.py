# Zwei Dictionarys
alter1 = {"Julias":28, "Peter:":30}
alter2 = {"Peter":30, "Julias:":28}

# Vergleich
if alter1 == alter2:
    print("Die Dics sind gleich")
try:
    if alter1 < alter2:
        print("1 < 2")
    else:
        print("nicht 1 < 2")
except:
    print("Fehler")