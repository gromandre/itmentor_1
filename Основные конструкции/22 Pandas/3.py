'''
    Найдите возрастную группу, представители которой чаще являются агентами, не используя фильтрацию. Возрастные группы:
        0-35: Young
        36-55: Middle-aged
        56+: Senior
'''

import pandas as pd
df = pd.read_csv('3.3.2.csv', sep=';')

try:
    df['age_group'] = pd.cut(
        df['Agent age'],
        bins=[0, 35, 55, float('inf')],
        labels=['Young', 'Middle-aged', 'Senior']
    )

    group_counts = df.groupby('age_group', observed=False).size()

    most_common_group = group_counts.idxmax()

    print(group_counts)
    print('Чаще всего агентами являются:', most_common_group)
except Exception as e:
    print(e)