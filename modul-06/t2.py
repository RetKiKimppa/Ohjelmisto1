import random

def noppa(tahkot):
    tulos = random.randint(1, tahkot)
    return tulos

maksimisilmaluku = int(input("Anna maksimisilmäluku esim. 1 - 21: "))

while True:
    heitto = noppa(maksimisilmaluku)
    if heitto == maksimisilmaluku:
        print(f"{heitto} -Maksimisilmälukusi.")
        break
    else:
        print(heitto)