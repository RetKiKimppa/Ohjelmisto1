sk_kanta = input("Syötä suorakulmion kanta: ")
sk_korkeus = input("Syötä suorakulmion korkeus: ")

sk_ala = float(sk_kanta) * float(sk_korkeus)
sk_piiri = float(sk_kanta) * 2 + float(sk_korkeus) * 2

print(f"Suorakulmion pinta-ala: {sk_ala}")
print(f"Suorakulmion piiri: {sk_piiri}")