yritys = 0

while True:
    user = input("Anna käyttäjätunnus: ")
    passw = input("Anna salasana: ")
    yritys += 1

    if yritys < 5:

        if user != "python" or passw != "rules":
            print("Yritä uudelleen")

        elif user == "python" or passw == "rules":
            print("Tervetuloa")
            break

    else:
        print("Pääsy evätty")
        break