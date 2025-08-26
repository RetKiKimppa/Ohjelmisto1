print("Kerro ikäsi tietääksesi voitko äänestää vaaleissa.")
ika = int( input("Anna ikä: ") )

if ika >= 18:
    print ("Voit äänestää vaaleissa")
else:
    print (f"Sinun tulee odottaa vielä {18 - ika} vuotta.")