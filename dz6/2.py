'''
Дана последовательность чисел. Получить список уникальных
элементов заданной последовательности, список повторяемых
и убрать дубликаты из заданной последовательности.

Пример:
[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]
'''
numbers = [1, 2, 3, 5, 1, 5, 3, 10]

uni = list(filter(lambda x: numbers.count(x) == 1, numbers))

rep = set(filter(lambda x: numbers.count(x) == 2, numbers))

rep = list(rep)

orig = list(set(numbers))

print(' уникальные ', uni)

print(' повторяемые ', rep)

print(' без дубликатов ', orig)
