import numpy as np
import pandas as pd
'''
~ - not
& - and
|-or
'''

'''Making dataset'''
data =pd.Series([2,3,54,10],index=['Tom','John','Ivan','Dallas'])


data.name='People and theirs age'
# print(data)
# print(data.values)
# print(data['Tom'])
# print(data.iloc[-1]) #choice by index
# not_tom = data.drop(index='Tom') #Skip Tom
# more_5= data[data>2].sort_values(ascending=False)
# john_dallas= data['John':'Dallas']
#
# print(not_tom)
# print(more_5)
# print(john_dallas)
'Фильтрация данных  без значений'
'''np.nan - Not a Number'''
'''Numpy'''
a = np.array([1, 2, 3, np.nan, np.nan, 4])
a= a[~np.isnan(a)]

b=a.sum()
print(a)
print('b=',b)
'''Pandas'''
c= pd.Series([1,2,3,np.nan,np.nan,5])
c=c[~np.isnan(c)] # может применять метод numpy
c=c.dropna() #свой метод от pandas
print(c)

new_data =pd.DataFrame({
    'Column A': [1, np.nan, 7],
    'Column B': [np.nan, 2, 3],
    'Column C': [np.nan, 2, np.nan]
})



'''Checking for null /not_null data in DataFrame'''
check_null_data=pd.isnull(new_data)
sum_not_null_data=pd.notna(new_data).sum()
print(new_data)
print(check_null_data)
print(sum_not_null_data)
'''Fill empty DATA'''

new_data = new_data.fillna(method='ffill') # Заполнить по верхнему значению
print(new_data)

