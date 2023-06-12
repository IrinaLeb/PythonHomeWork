# Написать EDA для датасета про пингвинов
# Необходимо:
# ● Использовать 2-3 точечных графика
# ● Применить доп измерение в точечных графиках, используя аргументы hue, size, stile
# ● Использовать 2-3 гистограммы

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

file = 'Seminar\penguins.csv'
df = pd.read_csv(file)

# species(вид пингвинов), island(остров), bill_length_mm(длина клюва), bill_depth_mm(глубина клюва), flipper_length_mm(длина ласты),
# body_mass_g(масса тела), sex(пол),

# print(df.head())
# print(df.columns)
# print(df.describe())

# sns.scatterplot(data=df, x='species', y='island') #какой вид пингвинов на каих островах
# plt.show()

# sns.scatterplot(data=df, x='bill_length_mm', y='species') # у каких видов пингвинов, какая длина клювов
# plt.show()

# sns.scatterplot(data=df, x='bill_length_mm', y='bill_depth_mm', hue='bill_length_mm', size='bill_length_mm', sizes=(2, 100)) #длина\глубина клюва по оттенкам и размерам
# plt.show()

# sns.scatterplot(data=df, x='bill_length_mm', y='flipper_length_mm', hue='flipper_length_mm', size='flipper_length_mm', sizes=(2, 100)) #длина ласт по оттенкам и размерам
# plt.show()

# sns.scatterplot(data=df, x='sex', y='bill_length_mm', hue='bill_length_mm', size='bill_length_mm', sizes=(2, 100)) #пол\длина клюва по оттенкам и размерам
# plt.show()

# ● Использовать PairGrid с типом графика на ваш выбор:

# cols = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'] #несколько графиков
# g = sns.PairGrid(df[cols])
# g.map(sns.scatterplot)
# plt.show()

# ● Изобразить Heatmap (температурная карта)

# sns.heatmap(data=df[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']], annot = True)
# plt.show()

# cols = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
# sns.heatmap(data=df[cols], annot=True)
# plt.show()

# sns.heatmap(data=df.corr(numeric_only=True), annot=True, vmin=-1, vmax=1, center=0)
# plt.show()