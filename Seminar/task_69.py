# Изобразить гистограмму по flipper_length_mm с оттенком height_group. Сделать анализ


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

file = 'Seminar\penguins.csv'
df = pd.read_csv(file)

df.loc[df['flipper_length_mm'] <= 190, 'height_group'] = 'low'
df.loc[(df['flipper_length_mm'] > 190) & (df['flipper_length_mm'] <= 210), 'height_group'] = 'middle'
df.loc[df['flipper_length_mm'] > 210, 'height_group'] = 'high'

print(df[['flipper_length_mm', 'height_group']])
print(df.groupby('height_group')['flipper_length_mm'].mean())
# df.groupby('height_group')['flipper_length_mm'].mean().plot(kind='bar')
sns.histplot(data=df, x='flipper_length_mm', hue='height_group')
plt.show()