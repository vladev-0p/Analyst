import sqlite3 as sq3
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
conn = sq3.connect('work_with_pandas.db')



cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS users(
    id integer primary key,
    name TEXT NOT NULL,
    salary integer NOT NULL)
''')

conn.commit()
users = [

    ('Daniel', 25000),

]
cur.executemany('''
INSERT INTO users (name,salary)
VALUES (?,?)
''',users)
conn.commit()
engine= create_engine('sqlite:///work_with_pandas.db')
'''Checking last 3 rows in db.users'''
table_user = pd.read_sql_table('users', engine)
conn.close()
# print([table_user.iloc[-3:,:]])

x=table_user.to_numpy()
plt.bar(table_user['name'],table_user['salary'])
plt.show()
print(x[-3:,:])
