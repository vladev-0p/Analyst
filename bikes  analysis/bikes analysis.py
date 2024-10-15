import pandas as pd
import matplotlib.pyplot as plt
bikes = pd.read_csv('london_merged.csv')

bikes.info()

weather = bikes.groupby('weather_code').size().sort_values(ascending=False)

print(weather)

season = bikes.groupby('season').size().sort_values(ascending=False)

print(season)

new_col_names = {
    'timestamp': 'time',
    'cnt': 'count',
    't1': 'temp_real_C',
    't2': 'temp_feels_like_C',
    'hum': 'humidity_percent',
    'wind_speed': 'wind_speed_km/h',
    'weather_code': 'weather',
}

bikes.rename(new_col_names, axis=1, inplace=True)

bikes.info()

'Change values in column'

season_rename = {
    '0.0': 'spring',
    '1.0': 'summer',
    '2.0': 'autumn',
    '3.0': 'winter',
}
'''Changing type  and rename of data'''
bikes['season'] = bikes['season'].astype('str').replace(season_rename)

print(bikes['season'])

print(bikes.groupby('season').size())

weather_dict = {
    '1.0': 'Clear',
    '2.0': 'Scattered clouds',
    '3.0': 'Broken clouds',
    '4.0': 'Cloudly',
    '7.0': 'Rain',
    '10.0': 'Rain with thunderstorm',
    '26.0': 'Snowfall'
}

bikes['weather'] = bikes['weather'].astype('str').map(weather_dict)
'''Show unique values as DataFrame'''
print(bikes[['weather']].drop_duplicates())

bikes.to_excel('london_bikes.xlsx', sheet_name='Data')


data = pd.read_excel('london_bikes.xlsx')
tmp = data['temp_real_C']
wind = data['wind_speed_km/h']
athletes= data['count']

plt.scatter(wind , tmp, s=athletes, alpha=0.006, c='red')

#
plt.ylabel('Temperature (°C)')
plt.xlabel('Wind speed (км/ч)')

# Название графика
plt.title('Количество спортсменов в зависимости от температуры и скорости ветра')

# Отображение графика
plt.show()