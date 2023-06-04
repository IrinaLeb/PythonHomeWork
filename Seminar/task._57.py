# 1. Прочесть с помощью pandas файл california_housing_test.csv, который находится в папке sample_data
# 2. Посмотреть сколько в нем строк и столбцов
# 3. Определить какой тип данных имеют столбцы

import pandas as pd
df = pd.read_csv('Seminar\california_housing_train.csv')

# print(df.head(5))

# print(df[df['housing_median_age'] < 20][['total_bedrooms', 'total_rooms']])

print(df.shape)
print(df.dtypes)