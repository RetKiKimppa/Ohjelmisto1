banaani = 2.85
omena = 3.15
appelsiini = 4.05

banaanikg = input("Anna banaanien määrä (kg): ")
omenakg = input("Anna omenoiden määrä (kg): ")
appelsiinikg = input("Anna appelsiinien määrä (kg): ")

banaanihinta = float(banaanikg) * banaani
omenahinta = float(omenakg) * omena
appelsiinihinta = float(appelsiinikg) * appelsiini
summa = banaanihinta + omenahinta + appelsiinihinta

print("Ostosten yhteenveto.")
print(f"Banaanit: {banaanihinta}€")
print(f"Omenat: {omenahinta}€")
print(f"Appelsiini: {appelsiinihinta}€")
print(f"Yhteensä: {summa} €")
