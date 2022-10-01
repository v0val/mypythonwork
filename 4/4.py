from random import randint
chisla = open("file.txt", 'r')
pos1 = int(chisla.readline().rstrip())
pos2 = int(chisla.readline().rstrip())
while True:
    n = int(input(f'введите количество элементов списка > {pos2}  '))
    if n > pos2: break
    print(f'веденое значение <={pos2}  ')
a = []
p = 1
for i in range(n):
    a.append(randint(-n, n))
print(a)
print(a[pos1]*a[pos2])
chisla.close()
    
