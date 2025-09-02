kaupungit = []

for x in range(5):
    kaupunki = input(f"Syötä kaupunki {x+1}.: ")
    kaupungit.append(kaupunki)

for kaupunki in kaupungit:
    print(f"-{kaupunki}")