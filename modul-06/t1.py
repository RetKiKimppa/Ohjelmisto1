import random

def noppa():
    tulos = random.randint(1,6)
    return tulos

while True:
    heitto = noppa()
    if heitto == 6:
        print("6 napsahti")
        break
    else:
        print(heitto)