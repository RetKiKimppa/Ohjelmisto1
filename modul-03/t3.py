sukupuoli = input("Oletko nainen vai mies?: ")
hemoglobiini = float(input("Kerrotko vielä hemoglobiini arvosi? (g/L): "))


if sukupuoli == "mies" and 196 > hemoglobiini > 133 :
    print("normaali taso mihelle")
elif sukupuoli  == "mies" and hemoglobiini < 134:
    print("alhainen taso miehlle")
elif sukupuoli == "mies" and hemoglobiini > 195:
    print("korkea taso miehlle")

elif sukupuoli == "nainen" and 176 > hemoglobiini > 116 :
    print("normaali taso naiselle")
elif sukupuoli  == "nainen" and hemoglobiini < 134:
    print("alhainen taso naiselle")
elif sukupuoli == "nainen" and hemoglobiini > 195:
    print("korkea taso naiselle")
else:
    print("Väärä vastaus")