print("Anna kolme kokonaislukua saadaksesi niistä summan, tulon ja keskiarvon!")

luku1 = input("Ensimmäinen kokonaisluku: ")
luku2 = input("Toinen kokonaisluku: ")
luku3 = input("Kolmas kokonaisluku: ")

luku_summa = int(luku1) + int(luku2) + int(luku3)
luku_tulo = int(luku1) * int(luku2) * int(luku3)
luku_ka = luku_summa / 3

print(f"Lukujen summa: {luku_summa}")
print(f"Lukujen tulo: {luku_tulo}")
print(f"Lukujen keskiarvo: {luku_ka}")