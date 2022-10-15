from postgres_table import create_tables

cur, conn = create_tables()

# sql2 = '''COPY airline_safety(name,available_seats,incidents_to_99,accidents_to_99,fatalities_to_99,\
#         incidents_to_14,accidents_to_14,fatalities_to_14)
#         FROM 'C:/Users/waqas/AppData/Local/Temp/airline-safety.csv'
#         DELIMITER ','
#         CSV HEADER;'''

# the above method was giving me headaches for hours so found this on internet
# to import csv into our table
with open('C:\\Users\\waqas\\Desktop\\project\\airline-etl\\airlinesafety.csv', 'r') as f:
    # skip the header
    next(f)
    cur.copy_from(f,'airline_safety', sep = ',')


conn.commit()

# to fetch all data from our table
sql3 = '''SELECT * FROM airline_safety'''
cur.execute(sql3)
for i in cur.fetchall():
    print(i)

conn.close()




