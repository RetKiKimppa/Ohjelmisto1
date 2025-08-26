kuha = float(input("Kuhan pituus?: "))
alamitta = 37

if kuha >= alamitta:
    print("Kuha on tarpeeksi pitkä.")
elif kuha < alamitta:
    print(f"Laske kuha veteen, pituutta puuttuu {alamitta - kuha} cm.")
