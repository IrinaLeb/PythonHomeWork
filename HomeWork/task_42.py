# Узнать какая максимальная households в зоне минимального значения population

import pandas as pd
df = pd.read_csv('Seminar\california_housing_train.csv')

popul_min = df.population.min()
min_meaning = df[df.population == popul_min]
print(min_meaning)

hous_max = min_meaning['households'].max()
print("Максимальное значение: ", hous_max)