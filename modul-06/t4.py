def yhteenlaskija(lista):
    summa = 0
    for num in lista:
        summa += num
    return summa

def main():
    numerot = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(yhteenlaskija(numerot))

main()