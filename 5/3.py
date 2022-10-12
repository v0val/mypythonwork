# создаем поле 3*3 для игры в "крестики нолики"
pole = []
for i in range(3):
    pole.append(['| _ |'] * 3)


# функция вывода поля игры
def pol():
    for i in range(3):
        for j in range(3):
            print(pole[i][j], end='')
        print()


print('ознакомтесь с полем: ')
pol()
print('где ')
print('|(0,0)|(0, 1)|(0,2)|')
print('|(1,0)|(1, 1)|(1,2)|')
print('|(1,0)|(1, 1)|(2,2)|')
# X, Y - координаты хода 1 игрока, T, P - 2 игрока, i, j - счетчики ходов 1 и 2
X = []
Y = []
T = []
P = []
i = 0
j = 0
tup = []  # список кортежей сделаных ходов
while True:
    i += 1
    j += 1

    print('1 игрок, выберите адрес клетки для Х от 0 до 2 по первому и второму индексу')
    while True:
        x, y = map(int, input().split())
        if not ((x, y) in tuple(tup)): break
        print('клетка занята')
    pole[x][y] = '| X |'
    X.append(x)
    Y.append(y)
    tup.append((x, y))  # учет сделаных ходов
    pol()
    if i >= 3:
        if (X.count(1) == 3 or X.count(2) == 3 or X.count(0) == 3) or \
                ((X[0] == Y[0]) and (X[1] == Y[1]) and (X[2] == Y[2])) or \
                ((X[0] + Y[0] == 2) and (X[1] + Y[1] == 2) and (X[2] + Y[2] == 2)) or \
                (Y.count(1) == 3 or Y.count(2) == 3 or Y.count(0) == 3):
            print('Игрок 1 выиграл!')
            break

    print('2 игрок, выберите адрес клетки для О от 0 до 2 по первому и второму индексу')
    while True:
        t, p = map(int, input().split())
        if not ((t, p) in tuple(tup)): break
        print('клетка занята')
    pole[t][p] = '| O |'
    T.append(t)
    P.append(p)
    tup.append((t, p))
    pol()
    if j >= 3:
        if T.count(1) == 3 or T.count(2) == 3 or T.count(0) == 3 or \
                ((T[0] == P[0]) and (T[1] == P[1]) and (T[2] == P[2])) or \
                ((T[0] + P[0] == 2) and (T[1] + P[1] == 2) and (T[2] + P[2] == 2)) or \
                (P.count(1) == 3 or P.count(2) == 3 or P.count(0) == 3):
            print('Игрок 2 выиграл!')
            break
    if i + j > 7:
        print('ничья')
        break
print('игра окончена')
input()
