print("Vastaa uusi/haku/lopeta")

lentokentat = {}

while True:
    ohjelma = input("Haluatko syöttää uuden lentoaseman, hakea lentoaseman vai lopettaa: ")

    if ohjelma == "uusi":
        icao = input("Anna lentokentän ICAO-koodi: ")
        kentta = input("Anna lentokentän nimi: ")
        lentokentat[icao] = kentta
        print("Tiedot syötetty")

    elif ohjelma == "haku":
        icao = input("Kerro ICAO-koodi nimi: ")
        if icao in lentokentat:
            print(lentokentat[icao])
        else:
            print("Kyseisellä ICAO-koodilla ei löytynyt lentoasemia.")

    elif ohjelma == "lopeta":
        print("Ohjelma lopetettu.")
        break

    else:
        print("Sinun täytyy syöttää seuraavista vaihtoehdoista: uusi/haku/lopeta")
