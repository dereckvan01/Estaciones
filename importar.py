from sqlite3.dbapi2 import connect
import numpy as np
import sqlite3
import pandas as pd
from pandas import read_csv
from sqlalchemy import create_engine

file= 'valores.txt'
data2=np.loadtxt(file, skiprows=3 ,delimiter='\t',dtype=bytes).astype(str)
df = read_csv('valores.txt', encoding = "ISO-8859-1")
df.count()
print(df)
#conn = sqlite3.connect('tes_database')
# c =  conn.cursor()
# c.execute('create table if not exists (data2)')
# conn.commit
# conn.close()
engine = create_engine('sqlite:///save_pandas.db', echo=True)
sqlite_connection = engine.connect()

sqlite_table = "Datos"
df.to_sql(sqlite_table, sqlite_connection, if_exists='fail')

