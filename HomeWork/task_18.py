# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит 
# натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

num = (int(input("Введите число элементов в массиве: ")))
list = [] 
for i in range(num):
    list.append(int(input("Введите натуральное число: ")))
    i += i
number = (int(input("Введите число, к которому нужно найти близкий элемент по величине: ")))
el = list[0]
dif = abs(list[0] - number)
for i in range(1,num):
    if abs(list[i] - number) < dif:
        dif = abs(list[i] - number)
        el = list[i]
print(list)
print(f"{el} -> самый близкий по величине элемент к заданному числу {number}")