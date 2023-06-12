# Создать новый столбец в таблице с пингвинами, который будет отвечать за показатель длины клюва пингвина.
# high - длинный(от 42)
# middle - средний(от 35 до 42)
# low - маленький(до 35)

import matplotlib.pyplot as plt
import pandas as pd
# import seaborn as sns

file = 'Seminar\penguins.csv'
df = pd.read_csv(file)

# species(вид пингвинов), island(остров), bill_length_mm(длина клюва), bill_depth_mm(глубина клюва), flipper_length_mm(длина ласты),
# body_mass_g(масса тела), sex(пол)

df.loc[df['bill_length_mm'] <= 35, 'bill_len'] = 'low'
df.loc[(df['bill_length_mm'] > 35) & (df['bill_length_mm'] <= 42), 'bill_len'] = 'middle'
df.loc[df['bill_length_mm'] > 42, 'bill_len'] = 'high'

print(df[['bill_length_mm', 'bill_len']])
print(df.groupby('bill_len')['bill_length_mm'].mean())
df.groupby('bill_len')['bill_length_mm'].mean().plot(kind='bar')
plt.show()