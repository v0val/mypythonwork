number = float(input('введите вещественное число '))
e = input('Введите точность вычисления ')
count_slice: int = len(e) - 2
print(round(number, count_slice))
