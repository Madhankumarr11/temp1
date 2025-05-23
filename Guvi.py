import psycopg2

connection = psycopg2.connect(
    host="localhost",
    port ='5432',
    user="postgres",
    password="01234"
)

cursor = connection.cursor()


cursor.execute("SELECT version()")

version = cursor.fetchone()

print("You are connected to - ", version)

connection.close()