import mysql.connector
yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='lentokentat',
         user='kim',
         password='1111',
         autocommit=True
         )

def lentokenttahaku(maa):
    sql = f"SELECT type, COUNT(*) AS maara FROM airport WHERE iso_country='{maa}' GROUP BY type ORDER BY maara DESC"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(F"Tyyppi:{rivi[0]} Määrä:{rivi[1]}")
    else:
        print("Tietoja ei löytynyt syötteellä.")
    return

haku = input("Anna maan tunnus (esim.FI), niin näet lentokentän tyypin: ")
lentokenttahaku(haku)
