from sqlalchemy import create_engine
import pandas as pd

host = 'localhost'
port = '5432'
user = 'postgres'
password = '01234'
database = 'pt_db'

connection = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')

df = pd.read_csv( 'bussiness.csv')

print(df)

table_name = 'Business'

df1 = df.to_sql('Business', connection, index=True, if_exists='replace')

print(df1)



