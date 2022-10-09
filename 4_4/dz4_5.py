f1 = open('filePoly1.txt')
f2 = open('filePoly2.txt')
polynom1 = f1.readline().strip()
f1.close()
polynom2 = f2.readline().strip()
f2.close()
print(polynom1)
print(polynom2)
# избавляюсь от пробелов
polynom1 = polynom1.replace(" ", "")
polynom2 = polynom2.replace(" ", "")
# делаю "костыли"
polynom1 = '+' + polynom1[:-2] + '*x^0'
polynom2 = '+' + polynom2[:-2] + '*x^0'
# выясняю какова максимальная степень многочлена, и определяю массив размерности этой степени
n1 = polynom1.find('^', 1, len(polynom1))
n2 = polynom2.find('^', 1, len(polynom2))
p1 = int(polynom1[n1 + 1])
p2 = int(polynom2[n2 + 1])
maxi = max(p1, p2)

# определяю размер списков (по максимуму)
mas1 = [0] * (maxi + 1)
mas2 = [0] * (maxi + 1)

# извлекаю коэфициенты многочлена и пишу их в список, (позиция = степени)
N = len(polynom1)
i = maxi + 1
tr = 0
while i != 0:
    p1 = polynom1.find('^', tr, N)
    z1 = polynom1.find('+', tr, N)
    z2 = polynom1.find('*', tr, N)
    i = int(polynom1[p1 + 1])
    mas1[i] = int(polynom1[z1 + 1:z2])
    tr = p1 + 1
    print(int(polynom1[p1 + 1]), polynom1[z1 + 1:z2])
print(mas1)

N = len(polynom2)
# можно было написать функцию
i = maxi + 1
tr = 0
while i != 0:
    p1 = polynom2.find('^', tr, N)
    z1 = polynom2.find('+', tr, N)
    z2 = polynom2.find('*', tr, N)
    i = int(polynom2[p1 + 1])
    mas2[i] = int(polynom2[z1 + 1:z2])
    tr = p1 + 1
    print(int(polynom2[p1 + 1]), polynom2[z1 + 1:z2])
print(mas2)

print('сумма коэфициентов: ')
for i in range(maxi + 1):
    mas1[i] = mas1[i] + mas2[i]
print(mas1)

# формируем многочлен (сумма исходных многочленов):

polynom = ''
for i in range(maxi, -1, -1):
    if i > 0 and mas1[i] != 0:
        polynom += str(mas1[i]) + '*x^' + str(i) + ' + '
    if i <= 0:
        polynom += str(mas1[i]) + ' = 0'
print(polynom)

f = open('fileSum.txt', 'w')
f.write(polynom)
f.close()
