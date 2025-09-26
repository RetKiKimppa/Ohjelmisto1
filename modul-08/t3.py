import mysql.connector
from geopy.distance import geodesic


yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='lentokentat',
         user='kim',
         password='1111',
         autocommit=True
         )

def lentokenttahaku(icao):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident='{icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    if tulos:
        return (tulos[0], tulos[1])
    else:
        return None

def etaisyyslasku(haku, uushaku):
    koord1 = lentokenttahaku(haku)
    koord2 = lentokenttahaku(uushaku)
    if not koord1 or not koord2:
        print("Jompaa kumpaa koodia ei löytynyt")
        return
    etaisyys = geodesic(koord1, koord2).kilometers
    print(f"Lentokenttien etäisyys on: {etaisyys:.2f}km")


haku = input("Anna eka icao-koodi: ").strip().upper()
uushaku = input("Anna toka icao-koodi: ").strip().upper()

etaisyyslasku(haku, uushaku)