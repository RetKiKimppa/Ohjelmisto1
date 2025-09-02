def pitkat_nimet(elaimet):
    long_names = []
    for elain in elaimet:
        if len(elain) > 6:
            long_names.append(elain)

    return long_names


elukat = ["kissa", "koira", "elefantti", "leijona", "kirahvi"]
loppu_elukat = pitkat_nimet(elukat)

print(elukat)
print(loppu_elukat)