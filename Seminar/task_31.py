# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где 
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

def nums_fib(n):
    print(n)
    if n == 0 or n == 1:
        return 1
    return nums_fib(n - 1) + nums_fib(n - 2)
print(nums_fib(7))