"""
Задайте натуральное число N.
Напишите программу, которая составит список
простых множителей числа N.
"""


def simple_number(x):
    count = 0
    k = 2
    while k <= x // 2:
        if x % k == 0:
            count += 1
        k += 1
    if count != 0:
        return False
    else:
        return True


lst_mult = [1]
N = int(input('Введите натуральное число '))

for i in range(2, N // 2 + 1):
    if N % i == 0 and simple_number(i):
        lst_mult.append(i)
print(lst_mult)
