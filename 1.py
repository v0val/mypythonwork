y = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
s = 0
x =input()
for i in x:
    if i in y:
        s +=int(i)
print(s)
