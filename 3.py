n = int(input('введите количество чисел последовательности '))
all_chisla = []
summ = 0
for i in range(1, n+1):
    elem = (1 + 1/i)**i
    all_chisla.append(elem)
    summ += elem
print(summ)
