import psycopg2

connection = psycopg2.connect(
    host="localhost",
    port = "5432",
    user="postgres",
    password="01234"
)

cursor = connection.cursor()


cursor.execute("select version()")

version = cursor.fetchone()

print(version)

connection.close()