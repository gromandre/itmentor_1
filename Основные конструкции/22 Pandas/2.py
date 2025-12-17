'''
    2) Найдите среднее, медиану и стандартное отклонение у округленных до целого значений df['Price'].
    Ответы округлите до десятых и выпишите их через пробел.
'''

import pandas as pd
df = pd.read_csv('3.3.2.csv', sep=';')

mean_price = (df['Price'].round(0).mean()).round(2)
median_price = (df['Price'].round(0).median()).round(2)
std_price = (df['Price'].round(0).std()).round(2)

print(mean_price, median_price, std_price, sep=' ')