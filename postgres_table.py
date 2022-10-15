import psycopg2

# connecting to newly created database
try:
    conn = psycopg2.connect(database = "airline", user = "postgres", password = "Immortalmk03@", host = "localhost", port = "5432")
except psycopg2.Error as e:
    print(e)

# setting autocommit to true
conn.autocommit = True

# creating cursor object
cursor = conn.cursor()


def create_tables():
    sql = '''CREATE TABLE IF NOT EXISTS AIRLINE_SAFETY(
            NAME VARCHAR(256),
            AVAILABLE_SEATS BIGINT,
            INCIDENTS_TO_99 BIGINT,
            ACCIDENTS_TO_99 BIGINT,
            FATALITIES_TO_99 BIGINT,
            INCIDENTS_TO_14 BIGINT,
            ACCIDENTS_TO_14 BIGINT,
            FATALITIES_TO_14 BIGINT
    )'''
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(sql)
    print("Table created successfully........")
    

    return cur, conn
    
if __name__ == '__main__':
    create_tables()




