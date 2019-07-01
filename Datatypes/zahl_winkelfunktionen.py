# Modul math
import math

# Trigonomische Funktionen
x = 30
# Umwandlung von Grad in Bogenmaß mithilfe von radians() // degrees() ermöglicht die Umwandlung von Bogenmaß in Grad.
xbm = math.radians(x) 
print("Sinus   ", x, "Grad:", math.sin(xbm))
print("Cosinus ", x, "Grad:", math.cos(xbm))
print("Tangens ", x, "Grad:", math.tan(xbm))
