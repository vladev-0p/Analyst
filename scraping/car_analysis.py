import pandas
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
'''SEARCHING FOR a CAR'''
url = 'https://www.autotrader.com/cars-for-sale/new-cars/bmw'

db = []
params = {
    'endYear': 2024,
    'newSearch': True,
    'startYear': 2021,

}

df = pd.DataFrame(columns=['Name', 'Price'])

response = requests.get(url, params=params)

soup = BeautifulSoup(response.content, 'lxml')
i = 0
# Searching tag with attr data-cmp="firstPrice"
name = soup.find_all('h2', attrs={"data-cmp": "subheading"})
price = soup.find_all(attrs={"data-cmp": "firstPrice"})
for name_tag, price_tag in zip(name, price):
    name = name_tag.text.strip()
    price = price_tag.text.strip()
    price_int = int(''.join(filter(str.isdigit, price)))
    db.append(name + ':' + price) #Collecting info into list , just for example
    df = pd.concat([df, pd.DataFrame([{'Name': name, 'Price': price_int}])], ignore_index=True) # Filling the DataFrame

df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
df['iName'] = df.apply(lambda row: f'{row.name}_{row["Name"]}', axis=1)
print(db)
print(df)
print(df.dtypes)
# plt.bar(df_selected['iName'],df_selected['Price'])
filtered = df.loc[df['Price'] < 69000]
print(filtered)
plt.bar(filtered['iName'],filtered['Price'])
plt.show()
