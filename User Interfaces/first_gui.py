import tkinter
# Funktion zu Schaltflächen
def ende():
    main.destroy()

# Hauptfenster
main = tkinter.Tk()

# Schaltfläche Ende
b = tkinter.Button(main, text = "Ende", command = ende)
b.pack()

# Endlosschleife
main.mainloop()