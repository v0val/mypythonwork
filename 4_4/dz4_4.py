k = int(input('введите степень многочлена'))

from random import randint

polynom = ''

for i in range(k, -1, -1):
    if i > 0:
        polynom += str(randint(0, 100)) + '*x^' + str(i) + ' + '
    else:
        polynom += str(randint(0, 100)) + ' = 0'
print(polynom)
f = open('file.txt', 'w')
f.write(polynom)
f.close()
