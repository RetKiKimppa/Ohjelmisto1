import random
luku = random.randint(1, 10)

while True:
    arvaus = float(input("Anna luku väliltä 1-10: "))
    if arvaus > luku:
        print("Liian suuri arvaus")
    elif arvaus < luku:
        print("Liian pieni arvaus")
    else:
        print("Oikein")
        break