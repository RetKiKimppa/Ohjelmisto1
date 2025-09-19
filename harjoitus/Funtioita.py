def minipeli_trivia():
    kysymykset = [
        ("Mikä on Suomen pääkaupunki: ", "helsinki"),
        ("Kuka on Suomen presidentti: ", "alexander stubb"),
        ("Monta Metropoliaa on: ", "neljä"),
        ("Mitä lehmä juo: ", "vettä"),
        ("Mikä on paras kasino: ", "kasinosetä"),
    ]
    tulos = 0
    max_sakko =  2
    sakko = 0
    for kysymys, oikea_vastaus in kysymykset:
        vastaus = input(kysymys).strip().lower()
        if vastaus == oikea_vastaus:
            print("Oikein")
            tulos += 1
        else:
            print("Väärä vastaus")
            sakko += 1
            if sakko >= max_sakko:
                break
    print(f"Tulos: {tulos}/5")

minipeli_trivia()