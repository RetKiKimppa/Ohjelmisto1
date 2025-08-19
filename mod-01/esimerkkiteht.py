import math

ympyra_sade = input("Anna ympyrän säde: ")
nelionsivu = input("Anna neliön sivun pituus: ")

ympyra_ala = math.pi * float(ympyra_sade) ** 2
nelio_ala = float(nelionsivu) ** 2

#print("Ympyrän pinta-ala: " + str(ympyra_ala) + ".")
#print("Neliön pinta-ala: " + str(nelio_ala) + ".")

#tai näin

print(f"Ympyrän pinta-ala: {ympyra_ala}")
print(f"Neliön pinta-ala: {nelio_ala}")