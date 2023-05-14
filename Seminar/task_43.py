# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента, равные друг другу 
# образуют одну пару, которую необходимо посчитать. Вводится список чисел. Все числа списка находятся на разныхс строках.
# Ввод: 
# 1 2 3 2 3
# Вывод:
# 2

import random
len_items = input("Введите длину массива: ")
items = [random.randint(0, 20) for i in range(int(len_items))]
print(items)

def count_pairs(items):
    count = 0
    for i in set(items):
        count += items.count(i) // 2
    return count
print(count_pairs(items))