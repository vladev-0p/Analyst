import lxml
import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''Извлекаем таблицу с HTML (Extract table from HTML)'''

URL = 'https://en.wikipedia.org/wiki/G7'
table = pd.read_html(URL)
data = table[4]

'''Фильтр  по столбцу '''

population = data.filter(like='Member').join(data.filter(like='Population')).join(
    data.filter(like='PPP GDP (Int$ million)'))  #taking 2 cols double filter
mask = population.apply(lambda i: i.astype(str).str.contains('Total').any(), axis=1) #Droping row with word Total in row
population.drop(index=population[mask].index, inplace=True)
# print(population)
'''Adding values'''
row1 = pd.Series({'Member': 'China', 'Population (2022-2023)': 1425149003, 'PPP GDP (Int$ million)[141]': 35291015})
population = population._append(row1, ignore_index=True)
# print(population)
# city = population.iloc[1]
# print(city)
# print(population)
# print('-------')
# population['GDP/PPP']=population['PPP GDP (Int$ million)[141]']/population['Population (2022-2023)']*1000000
population['GDP/PPP'] = population.iloc[:, 2] / population.iloc[:, 1] * 1000000
# print(population.columns)
# print(population)
'''Making  graph'''
plt.bar(population['Member'], population['GDP/PPP'])
plt.show()
# print(population.head())


