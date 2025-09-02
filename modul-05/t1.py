import random
arpakuutio = int(input("Anna arpakuutioiden määrä: "))

summa = 0

for luku in range(arpakuutio):
    luku = random.randint(1, 6)
    summa += luku

print(summa)
