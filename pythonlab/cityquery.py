import psycopg2

def main():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="neiroukhm",
        user="neiroukhm",
        password="spring847eyebrow"
    )
    cursor = conn.cursor()

    # 1. Check if Northfield is present and print its location
    check_and_print_northfield(cursor)

    # 2. Print the name of the city with the largest population
    print_largest_population_city(cursor)

    # 3. Print the name of the city in Minnesota with the smallest population
    print_smallest_population_city_in_mn(cursor)

    # 4. Print out the names of the cities that are furthest in each direction
    print_extreme_cities(cursor)

    # 5. User input for state and print total population of all cities in that state
    state = input("Enter a state name or abbreviation: ")
    print_total_population_by_state(cursor, state)

    cursor.close()
    conn.close()

def check_and_print_northfield(cursor):
    cursor.execute("SELECT latitude, longitude FROM us_cities WHERE city = 'Northfield'")
    result = cursor.fetchone()
    if result:
        print(f"Northfield is located at Latitude: {result[0]}, Longitude: {result[1]}")
    else:
        print("Northfield is not present in the database.")

def print_largest_population_city(cursor):
    cursor.execute("SELECT city FROM us_cities ORDER BY population DESC LIMIT 1")
    result = cursor.fetchone()
    if result:
        print(f"The city with the largest population is {result[0]}.")

def print_smallest_population_city_in_mn(cursor):
    cursor.execute("SELECT city FROM us_cities WHERE state = 'Minnesota' ORDER BY population ASC LIMIT 1")
    result = cursor.fetchone()
    if result:
        print(f"The city in Minnesota with the smallest population is {result[0]}.")

def print_extreme_cities(cursor):
    directions = {
        "North": "latitude DESC",
        "East": "longitude DESC",
        "South": "latitude ASC",
        "West": "longitude ASC"
    }
    for direction, order in directions.items():
        cursor.execute(f"SELECT city FROM us_cities ORDER BY {order} LIMIT 1")
        result = cursor.fetchone()
        if result:
            print(f"The city furthest {direction} is {result[0]}.")

def print_total_population_by_state(cursor, state_input):
    cursor.execute("SELECT state_name FROM us_states WHERE state_code = %s OR state_name = %s", (state_input, state_input))
    state_name = cursor.fetchone()
    if state_name:
        cursor.execute("SELECT SUM(population) FROM us_cities WHERE state = %s", (state_name[0],))
        result = cursor.fetchone()
        print(f"Total population of all cities in {state_name[0]} is {result[0]}")
    else:
        print("Invalid state name or abbreviation.")

if __name__ == "__main__":
    main()

