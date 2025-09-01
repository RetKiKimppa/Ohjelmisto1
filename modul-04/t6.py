import random

N = int(input("Kuinka monta pistettä arvotaan? "))
n = 0
kerrat = 0

while kerrat < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        n += 1
    kerrat += 1

pii_likiarvo = 4 * n / N

print(f"Piin likiarvo: {pii_likiarvo}")