import mysql.connector

yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="kim",
    password="1111",
    autocommit=True
)

def lentokenttahaku():
    sql = "SELECT * FROM game "
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

print(lentokenttahaku())