'''
    1) Найдите час, в который чаще всего совершались сделки.
    (Подсказка: из ячеек формата DateTime можно извлечь час с помощью .dt.hour; например data['Date'].dt.hour)
'''

import pandas as pd
df = pd.read_csv('3.3.2.csv', sep=';')



df['Time of deal'] = pd.to_datetime(df['Time of deal'])
hour = df['Time of deal'].dt.hour.value_counts().index[0]
amount_hour = df['Time of deal'].dt.hour.value_counts().iloc[0]

print(f'Час, в который чаще всего совершались сделки: \'{hour}\' - {amount_hour} сделок')





