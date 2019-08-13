# Module
import time
import threading

# Thread- Funktion


def show():
    print("Start Thread")
    for i in range(5):
        print(i, time.time())
        time.sleep(1.5)
    print("Ende Thread")
    return


# Main App

print("Start Hauptprogramm")
t1 = threading.Thread(target=show)
t1.start()
# time.sleep(10)
# t2 = threading.Thread(target=show)
# t2.start()

time.sleep(10)
print("Ende Hauptprogramm")