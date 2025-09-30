from enum import Enum
import mysql.connector
import os
import math
from dataclasses import dataclass
from geopy.distance import geodesic

conn = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='bosstest',
         user='kim',
         password='1111',
         autocommit=True
         )


class Difficulty(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

#user_name: str
#current_power: int = 100
#current_airport: Airport | None
#goal_airport: Airport | None
difficulty: Difficulty.EASY
#visited_airports: set[Airport]

#player_id = sql player_id

def start_game(user_name: str, difficulty:str):
    with conn.cursor() as cursor:
        cursor.execute("SELECT id FROM player WHERE name = %s", (user_name,))
        result = cursor.fetchone()

        #Checks if username exists
        if result:
            print("Username already exists")
        else:
            #Creates new user
            cursor.execute("INSERT INTO player(name, difficulty_level) VALUES (%s, %s)", (user_name, difficulty))
            print("Username created")

            cursor.execute("""SELECT id FROM player WHERE name = %s""", (user_name,))


def load_game(user_name: str):
    with conn.cursor() as cursor:
        cursor.execute("SELECT id FROM player WHERE name = %s", (user_name,))
        result = cursor.fetchone()


def get_country_names():
    with conn.cursor() as cursor:
        cursor.execute("""
                SELECT DISTINCT country_name 
                FROM country
                JOIN airport ON aiport.iso_country = country.iso_country""")
        result = cursor.fetchall()
        return result


def get_country_name(user_name: str):
    with conn.cursor() as cursor:
        cursor.execute("""
                SELECT country.name
                FROM player
                JOIN players_airports ON player.id = player_id
                JOIN airport ON airport_ident = airport.ident
                JOIN country ON airport.iso_country = country.iso_country
                WHERE player.name = %s
                       """, (user_name,))

        result = cursor.fetchone()

        if result:
            print(result)
            return result[0]  # palauttaa maan nimen
        else:
            return None






def get_a_port_name(country_name:str):
    with conn.cursor() as cursor:
        cursor.execute("""
                SELECT airport.name
                FROM airport
                JOIN country ON airport.iso_country = country.iso_country
                WHERE country.name = %s
                       """, (country_name,))

        result = cursor.fetchone()

        if result:
            return result[0]  # Return airport name
        else:
            return None


def get_distance_to_goal_km():




#def get_challenge():

#def challenge_complete(success: bool): -> int


def select_location(country: str, user_name: str):
    with conn.cursor() as cursor:
        cursor.execute("""
                       UPDATE player
                       SET current_location
                       """, (user_name,))




