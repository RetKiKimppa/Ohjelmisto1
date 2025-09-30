import mysql.connector
import os
import math
from dataclasses import dataclass
from dotenv import load_dotenv
from mysql.connector import Error

load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv('db_host'),
    port=int(os.getenv('db_port', 3306)),
    database=os.getenv('db_name'),
    user=os.getenv('db_username'),
    password=os.getenv('db_password'),
    charset='utf8mb4',
    collation='utf8mb4_general_ci'
)


def change_country2(conn, player_id: int, country_name: str):
    with conn.cursor() as cursor:
        cursor.execute("SELECT current_location, battery_level FROM player WHERE id = %s", (player_id,))
        current_ident, battery = cursor.fetchone()

        # Hae nykyinen kenttä
        cursor.execute("""
            SELECT ident, name, latitude_deg, longitude_deg, iso_country
            FROM airport WHERE ident = %s
        """, (current_ident,))
        current_airport = Airport(*cursor.fetchone())

        # Hae uusi kenttä
        new_airport = Airport.from_country(country_name, conn)

        # Tarkista onko jo vierailtu
        cursor.execute("""
            SELECT 1 FROM players_airports WHERE player_id = %s AND airport_ident = %s
        """, (player_id, new_airport.ident))
        if cursor.fetchone():
            print("Olet jo käynyt tässä maassa.")
            return

        distance = Airport.distance_km(current_airport, new_airport)
        direction = Airport.direction(current_airport, new_airport)
        battery_cost = int(distance / 50)

        if battery < battery_cost:
            print("Ei tarpeeksi akkua.")
            return

        # Päivitä pelaajan sijainti ja akku
        cursor.execute("""
            UPDATE player SET current_location = %s, battery_level = battery_level - %s WHERE id = %s
        """, (new_airport.ident, battery_cost, player_id))

        # Lisää uusi kenttä players_airports-tauluun
        cursor.execute("""
            SELECT COUNT(*) FROM players_airports WHERE player_id = %s;
        """, (player_id,))
        sequence = cur.fetchone()[0] + 1

        cursor.execute("""
            INSERT INTO players_airports (player_id, airport_ident, is_starting_airport, is_boss_airport, battery_cost, order_sequence, visited_at)
            VALUES (%s, %s, FALSE, FALSE, %s, %s, NOW());
        """, (player_id, new_airport.ident, battery_cost, sequence))

    conn.commit()
    print(f"Lensit kentälle {new_airport.name} ({new_airport.iso_country}), suunta: {direction.name}, akun taso: {battery - battery_cost}")


def change_country()