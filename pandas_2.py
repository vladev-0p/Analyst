import pandas as pd

info = pd.DataFrame({
    'Occupation': ['stud', 'worker', 'unemployed'],
    'Age': [20, 23, 24],
})

info.index = ['Alex', 'Bob', 'Ivan']
info['Country'] = 'USA'
print(info.iloc[2])
print(info.loc['Alex'])
print(info)
'''Changing name of columns'''
info.rename(
    columns={
        'Age': 'YEARS',
        'Occupation':'Employment',
    },inplace=True)
print(info)
print(info)
