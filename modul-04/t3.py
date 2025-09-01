luku = input("Anna luku: ")

if luku != "":
    arvo = float(luku)
    suurin = arvo
    pienin = arvo

    while True:
        luku = input("Anna luku: ")
        if luku == "":
            print(f"Suurin luku: {suurin}, pienin luku: {pienin}")
            break
        elif float(luku) > suurin:
            suurin = float(luku)
        elif float(luku) < pienin:
            pienin = float(luku)

elif luku == "":
    print("Anna edes yksi luku")