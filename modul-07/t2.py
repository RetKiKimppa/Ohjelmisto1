nimet = set()

while True:
    nimi = input("Anna nimi(tyhjä, lopettaa ohjelman): ")
    if nimi == "":
        break
    elif nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)

print("Syötetyt nimet:")
for name in nimet:
    print(name)