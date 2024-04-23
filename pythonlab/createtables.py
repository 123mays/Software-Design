import psycopg2
def create_tables():
    commands = [
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
    conn = None
    try:
        conn = psycopg2.connect(
            dbname='yourdbname', user='yourusername', password='yourpassword', host='yourhost'
        )
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not limited:
            conn.close()

if __name__ == '__main__':
    create_tables()

