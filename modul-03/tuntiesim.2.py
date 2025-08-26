print("Sähkönkulutus hinta-arvio. ")
sähkökulutus = float(input("Monta kWh: "))

if sähkökulutus <= 0:
    print("Sähkösi ei maksa mitään")
    hinta = 0.0

elif sähkökulutus <= 50:
    hinta = 0.10 * sähkökulutus

elif sähkökulutus <= 200:
    hintaA = 50 * 0.10
    yli50kwh = sähkökulutus - 50
    hintaB = yli50kwh * 0.08
    hinta = hintaA + hintaB

elif sähkökulutus > 200:
    hintaA = 50 * 0.10
    hintaB = 150 * 0.08
    yli200kwh = sähkökulutus - 200
    hintaC = yli200kwh * 0.06
    hinta = hintaA + hintaB + hintaC

print(f"Hinta on {hinta} euroa.")