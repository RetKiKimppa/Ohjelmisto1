import math

leiviska = input("Anna leiviskät: ")
naula = input("Anna naulat: ")
luoti = input("Anna luodit: ")

leiviska_luodit = float(leiviska) * 20 * 32
naula_luodit = float(naula) * 32
kokonaisluodit = naula_luodit + leiviska_luodit + float(luoti)
kokonaisgramma = kokonaisluodit * 13.3

kilogramma = kokonaisgramma // 1000
grammat = kokonaisgramma % 1000

print("Massa nykymittojen mukaan: " )
print(f"{kilogramma} kilogrammaa ja {grammat:.2f} grammaa.")