# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве), 
# которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива. 
# Затем число M - количество элементов во втором массиве. Затем элементы второго массива
# Ввод: 
# 7 
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)
# Вывод:
# 3 3 2 12

def nums_list(n):
    result_list = []
    for i in range(n):
        result_list.append(int(input("Введите элемент: ")))
    return result_list

def new_List():
    list_1 = input("Введите элементы массива через пробел: ").split()
    for k in range(len(list_1)):
       list_1[k] = list_1[k]
    return list_1

def dif_list(list_a, list_b):
    list_c = []
    for i in list_a:
        if i not in list_b:
            list_c.append(i)
    return list_c
list_1 = (nums_list(7))
list_2 = (new_List())
print(dif_list(list_1, list_2))        