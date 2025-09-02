def gallona_litroiksi(bensa):
    litra = bensa * 3.785
    return litra

while True:
    gallona = float(input("Ilmoita bensiinin määrä gallonoina: "))
    if gallona > -1:
        print(f"Teillä on {gallona_litroiksi(gallona)} litraa bensiiniä")
    else:
        break