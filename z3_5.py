n = int(input())
f1 = 0
f2 = 1
a = []
a.append(f1)
a.append(f2)
k = 2
while k < 2*(n // 2 + 1): #доработать количество
    f1 = f1 + f2
    f2 = f1 + f2
    a.append(f1)
    a.append(f2)
    k += 2
print(a)
b = list(reversed(a))
for i in range(0,len(b),2):
    b[i] *= -1
b = b[:] + a[1:]
print(b)
    
    
    
