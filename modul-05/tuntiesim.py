numero = int(input("Anna numero: "))
luvut = []

while numero >= 0:
    luvut.append(numero)
    numero = int(input("Anna numero: "))

luvut.sort()
print(luvut)

if 10 in luvut:
    print("Numero 10 löytyi")
else:
    print("Numeroa 10 ei löytynyt")