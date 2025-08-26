sukupuoli = input("Oletko nainen vai mies?: ")
hemoglobiini = float(input("Kerrotko vielä hemoglobiini arvosi? (g/L): "))


if sukupuoli == "mies" and 196 > hemoglobiini > 134 :
    print("normaali taso mihelle")
elif sukupuoli  == "mies" and hemoglobiini < 134:
    print("alhainen taso miehlle")
elif sukupuoli == "mies" and hemoglobiini > 195:
    print("korkea taso miehlle")
