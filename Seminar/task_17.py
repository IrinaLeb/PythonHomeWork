# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

n = int(input ("Введите величину списка = "))
n_digits = [int(input("Введите числа: ")) for i in range(n)]
print(n_digits)
n_digits = set(n_digits)
print(n_digits)
print(len(n_digits))
