import psycopg2

def create_tables_and_load_data():
    table_commands = [
        """
        CREATE TABLE us_cities (
            city VARCHAR(100),
            state VARCHAR(100),
            population INTEGER,
            latitude FLOAT,
            longitude FLOAT
        );
        """,
        """
        CREATE TABLE us_states (
            state_code VARCHAR(2),
            state_name VARCHAR(100),
            population INTEGER
        );
        """
    ]
    
    copy_commands = [
        """
        COPY us_cities(city, state, population, latitude, longitude)
        FROM '../us-cities-top-1k.csv' 
        DELIMITER ',' 
        CSV HEADER;
        """,
        """
        COPY us_states(state_code, state_name, population)
        FROM '../us-state-pop.csv' 
        DELIMITER ',' 
        CSV HEADER;
        """
    ]
    
    
if __name__ == '__main__':
    create_tables_and_load_data()
