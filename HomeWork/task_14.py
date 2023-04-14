# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

number = int(input("Введите число  N = "))
n = 0
i = 0
while n < number:   
    n = 2**i   
    if n > number:
        break
    print(n)
    i += 1