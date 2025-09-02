loppu = int(input("Anna numero: "))

if loppu >= 0:
    for luku in range(2, loppu+1, 2):
        print(luku)
else:
    for luku in range(-2, loppu-1, -2):
        print(luku)