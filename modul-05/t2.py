luku_str = input("Anna kokonaisluku, (Pelkkä enter lopettaa toiminnon): ")
luvut =[]

while luku_str != "":
    luku = int(luku_str)
    luvut.append(luku)
    luku_str = input("Anna kokonaisluku, (Pelkkä enter lopettaa toiminnon): ")

luvut.sort(reverse=True)

print(f"Viisi suurinta:  {luvut[0:5]}.")
