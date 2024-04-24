import psycopg2

# Function to create tables in the database
def create_tables():
    # Connection parameters - enter your details here
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="neiroukhm",
        user="neiroukhm",
        password="Spring847eyebro"
    )
    
    # Create a cursor object using the cursor() method
    cur = conn.cursor()

    # SQL for creating us_cities table
    create_us_cities = """
    CREATE TABLE IF NOT EXISTS us_cities (
        city VARCHAR(100),
        state VARCHAR(100),
        population INT,
        latitude FLOAT,
        longitude FLOAT
    );
    """

    # SQL for creating us_states table
    create_us_states = """
    CREATE TABLE IF NOT EXISTS us_states (
        state_code VARCHAR(2),
        state_name VARCHAR(100),
        population INT
    );
    """

    try:
        # Execute the SQL commands to create tables
        cur.execute(create_us_cities)
        cur.execute(create_us_states)

        # Commit the changes to the database
        conn.commit()
        print("Tables created successfully")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while creating tables:", error)

    finally:
        # Close the cursor and connection
        cur.close()
        conn.close()

# Call the function to create tables
create_tables()

