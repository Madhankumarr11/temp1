from sqlalchemy import create_engine
import pandas as pd   #reading file


host = 'localhost'
port = '5432'
user = 'postgres'
password = '01234'
database = 'py_db'

connection = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')

df = pd.read_csv( 'bussiness.csv')

table_name = 'bussiness'

# print(df)

df.to_sql(table_name, connection, index=False, if_exists='replace' )    #(if_exists="append","fail","replace")

# df.to_sql(table_name, engine,index=False,if_exists="replace")