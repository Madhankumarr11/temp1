import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT      #to do autocommit in database


connection = psycopg2.connect(
    host='localhost',
    user='postgres',
    password='01234',
    database='py_db'
)

connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

#cursor -> intermediator for python and postgres db
cursor = connection.cursor()

# cursor.execute('select version()')

# output = cursor.fetchone()
# print(output)

# inter = connection.cursor()

# inter.execute('select version()')

# output = inter.fetchone()
# print(output)

# # Close connection
# cursor.close()
# connection.close()

#======================================================================================================================

# cursor.execute('create Database py_db')

#======================================================================================================================

# creating table in 'py_db' database

# cursor.execute ('create table py_table (id int, name varchar(20))')

#======================================================================================================================

#Inserting data in table

# cursor.execute("insert into py_table (id, name) values(1,'madhan')")

#======================================================================================================================

#Read the table data

# cursor.execute('select * from py_table')

# output = cursor.fetchall()

# print(output)