import mysql.connector
yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='lentokentat',
         user='kim',
         password='1111',
         autocommit=True
         )

def lentokenttahaku(icao):
    sql = f"SELECT name FROM airport WHERE ident='{icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Lentokentän nimi: {rivi[0]}")
    else:
        print("Syötteelläsi ei löytyny tietoja")
    return

haku = input("Anna lentokentän ICAO-koodi, niin näet kentän nimen: ")
lentokenttahaku(haku)


