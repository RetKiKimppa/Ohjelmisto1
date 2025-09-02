def parilliset_muuntaja(lista):
    parilliset = []
    for num in lista:
        if num % 2 == 0:
            parilliset.append(num)

    return parilliset

def main():
    numerot = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    parilliset = parilliset_muuntaja(numerot)
    print(f"Alkuperäinen lista: {numerot}")
    print(f"Karsittu lista: {parilliset}")

main()