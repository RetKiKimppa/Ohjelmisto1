def trivia_peli():
    tulos = 0
    sakko = 0
    if sakko == 2:
        return
    print("Trivia peli: 5 kysymystä, vain 2 saa mennä väärin.")
    vastaus = input("Mikä on Suomen pääkaupunki: ")
    if vastaus == "Helsinki" or vastaus == "helsinki":
        print("Oikein")
        tulos += 1
        vastaus = input("Kuka on Suomen presidentti: ")
        if vastaus == "Alexander Stubb":
            print("Oikein")
            tulos += 1
        else:
            sakko += 1
    else:
        print("väärin")
        sakko += 1
        vastaus = input("Kuka on Suomen presidentti: ")
        if vastaus == "Alexander Stubb":
            print("Oikein")
            tulos += 1
        else:
            sakko += 1



def trivia_peli():
    kysymykset = [
        ("Mikä on Suomen pääkaupunki?", "helsinki"),
        ("Kuka on Suomen presidentti?", "alexander stubb"),
        ("Mikä on Suomen korkein vuori?", "halti"),
        ("Montako maakuntaa Suomessa on?", "19"),
        ("Mikä on Suomen kansalliseepos?", "kalevala")
    ]

    tulos = 0
    sakko = 0
    max_sakot = 2

    print("Trivia-peli: 5 kysymystä. Vain 2 saa mennä väärin.\n")

    for kysymys, oikea_vastaus in kysymykset:
        vastaus = input(kysymys + " ").strip().lower()
        if vastaus == oikea_vastaus:
            print("Oikein!\n")
            tulos += 1
        else:
            print("Väärin.\n")
            sakko += 1
            if sakko >= max_sakot:
                print("Liikaa vääriä vastauksia. Peli päättyy.")
                break

    print(f"Pisteesi: {tulos}/5")

trivia_peli()