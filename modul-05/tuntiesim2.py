luvut = []
tulos_luvut = []

arvo_str = input("Anna kokonaisluku: ")

while arvo_str != "":
    arvo = int(arvo_str)
    luvut.append(arvo)
    arvo_str = input("Anna kokonaisluku: ")
for luku in luvut:
    if luku not in tulos_luvut and luku > 100:
        tulos_luvut.append(luku)
        print(luku)