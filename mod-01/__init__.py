import mysql.connector

yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="",
    user="root",
    password="1202",
    autocommit=True
)

def lentokenttahaku():
    sql = "SELECT * FROM flight_game "
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

print(lentokenttahaku())