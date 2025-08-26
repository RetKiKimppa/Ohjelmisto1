print("Stipendi testeri.")

fysiikka = float(input ("Kerro fysiikan suorituspisteet: ") )
matikka = float(input ("Kerro matematiikan suorituspisteet: ") )
kemia = float(input ("Kerro kemian suorituspisteet: ") )

if fysiikka < 50 or matikka < 50 or kemia < 50:
    print("Et saanut stipendiä")
elif fysiikka and matikka > 90:
    print("Sait stipendin matematiikan ja fysiikan perusteella")
elif kemia > 95:
    print("Sait stipendin kemian perusteella")
else:
    print("Et saanut stipendiä")