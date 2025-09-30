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


@dataclass
class Airport:
    ident: str
    name: str
    latitude_deg: float
    longitude_deg: float
    iso_country: str

    @staticmethod
    def from_ident(conn, ident: str):
        cursor = conn.cursor()
        cursor.execute("""
            SELECT ident, name, latitude_deg, longitude_deg, iso_country
            FROM airport
            WHERE ident = %s
        """, (ident,))
        row = cursor.fetchone()
        cursor.close()
        return Airport(*row)

    @staticmethod
    def from_country(conn, country_name: str) -> 'Airport':
        cursor = conn.cursor()
        cursor.execute("""
            SELECT a.ident, a.name, a.latitude_deg, a.longitude_deg, a.iso_country
            FROM airport a
            JOIN country c ON a.iso_country = c.iso_country
            WHERE c.name = %s
            ORDER BY RAND()
            LIMIT 1
        """, (country_name,))
        row = cursor.fetchone()
        cursor.close()
        return Airport(*row)

    @staticmethod
    def distance_km(a: 'Airport', b: 'Airport') -> float:
        R = 6371
        lat1, lon1 = math.radians(a.latitude_deg), math.radians(a.longitude_deg)
        lat2, lon2 = math.radians(b.latitude_deg), math.radians(b.longitude_deg)
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        haversine = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        return 2 * R * math.asin(math.sqrt(haversine))

    @staticmethod
    def direction(from_: 'Airport', to: 'Airport') -> str:
        dx = to.longitude_deg - from_.longitude_deg
        dy = to.latitude_deg - from_.latitude_deg
        angle = math.degrees(math.atan2(dx, dy)) % 360
        directions = ["North", "North-East", "East", "South-East", "South", "South-West", "West", "North-West"]
        index = round(angle / 45) % 8
        return directions[index]




def change_country(conn, player_id: int, country_name: str):
    with conn.cursor() as cursor:
        cursor.execute("SELECT current_location, battery_level FROM player WHERE id = %s", (player_id,))
        current_ident, battery = cur.fetchone()

        # Hae nykyinen kenttä
        cursor.execute("""
            SELECT ident, name, latitude_deg, longitude_deg, iso_country
            FROM airport WHERE ident = %s
        """, (current_ident,))
        current_airport = Airport(*cur.fetchone())

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

