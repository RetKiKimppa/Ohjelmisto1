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
        return

#Finds airports using country names
def get_a_port_name(country_name:str):
    with conn.cursor() as cursor:
        cursor.execute("""
                SELECT airport.name
                FROM airport
                JOIN country ON airport.iso_country = country.iso_country
                WHERE country.name = %s
                       """, (country_name,))

        result = cursor.fetchall()

        if result:
            #If country has aiports, return all of them
            airports = result
            return airports
        else:
            #If not return none
            return None


# Returns a list of countries that have airports
def get_country_names():
    with conn.cursor() as cursor:
        cursor.execute("""
                SELECT DISTINCT country.name 
                FROM country
                JOIN airport ON airport.iso_country = country.iso_country""")
        result = cursor.fetchall()
        return [row[0] for row in result]