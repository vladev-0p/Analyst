import sqlite3 as sq3

import openpyxl
import pandas as pd
excel='fruits.xlsx'
df = pd.read_excel(excel)

report = df.groupby('Fruits', as_index=False).sum().rename(columns={'Amount':'total amount'})

with pd.ExcelWriter(excel, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    report.to_excel(writer, sheet_name='Summary Report', index=False)



con=sq3.connect('fruits.db')

cur=con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS fruits(
        id integer primary_key,
        Fruits Text ,
        Total amount integer
        )''')

con.commit()

report.to_sql('fruits',con, if_exists='replace',index=False)

con.close()