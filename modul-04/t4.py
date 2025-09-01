luku = input("Anna luku: ")

if luku != "":
    arvo = float(luku)
    suurin = float(arvo)
    pienin = float(arvo)

    while True:
           if float(luku) > suurin:
            suurin = float(suurin)
            print(f"Suurin: {suurin}, Pienin: {pienin}")

           elif float(luku) < pienin:
            pienin = float(pienin)
            print(f"Suurin: {suurin}, Pienin: {pienin}")

           elif luku == "":
               break
else:
    print("Et antanut lukua!")
