''' At this project we made function which  filters crypto data by specifically given parameters '''
import requests
import pandas as pd

# def get_historic_price(symbol, exchange='bitfinex', after='2018-09-01'):
#     url = f'https://api.cryptowat.ch/markets/{exchange}/{symbol}usd/ohlc'.format(
#         symbol=symbol,
#         exchange=exchange,
#     )
#     response = requests.get(url,
#                             params={
#                                 'periods': '3600',
#                                 'after': str(int(pd.Timestamp(after).timestamp()))
#                             })
#     response.raise_for_status()
#     data = response.json()
#     df = pd.DataFrame(data['result']['3600'],columns=[
#         'CloseTime', 'OpenPrice', 'HighPrice', 'LowPrice', 'ClosePrice', 'Volume', 'NA'
#     ])
#     df['CloseTime'] = pd.to_datetime(df['CloseTime'], unit='s')
#     df.set_index('CloseTime', inplace=True)
#     return df

'''Getting filtered info about Crypto'''


def get_data(s_name, **filters):
    df = pd.read_excel('cryptos.xlsx', sheet_name=s_name)
    for column, condition in filters.items():
        if isinstance(condition, dict):
            for operator, value in condition.items():
                if operator == 'range':
                    df = df[(df[column] >= value[0]) & (df[column] <= value[1])]
                elif operator == '+':
                    df = df[df[column] > value]
                elif operator == '-':
                    df = df[df[column] < value]
        else:
            return df.read()

    return df


filters = {'Volume': {'range': [0, 100]},
           'ClosePrice': {'+': 4000}
           }

x = get_data('Bitcoin', **filters)

print(x)
