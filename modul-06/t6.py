import math

def pizzalaskuri(p_koko, p_hinta):
    pinta_ala = (p_koko / 2) ** 2 * math.pi
    europer_m2 = p_hinta / (pinta_ala / 10000)
    return europer_m2

def main():
    ekakoko = float(input("Anna ensimmäisen pizzan halkaisija senttimetreinä: "))
    ekahinta = float(input("Anna vielä pizzan hinta euroina: "))

    tokakoko = float(input("Anna toisen pizzan halkaisija senttimetreinä: "))
    tokahinta = float(input("Anna vielä pizzan hinta euroina: "))

    yksikko1 = pizzalaskuri(ekakoko, ekahinta)
    yksikko2 = pizzalaskuri(tokakoko, tokahinta)

    print(f"Esimmäisen pizzan hinta on {yksikko1:.2f} €/m2")
    print(f"Toisen pizzan hinta on {yksikko2:.2f} €/m2")

    if yksikko1 > yksikko2:
        print("Pizzalla 2 on parempi hintalaatusuhde")
    elif yksikko1 < yksikko2:
        print("Pizzalla 1 on parempi hintalaatusuhde")
    else:
        print("Pizzoilla on yhtä hyvä hintalaatusuhde")

main()