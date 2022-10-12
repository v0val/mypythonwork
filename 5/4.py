from typing import TextIO

f: TextIO = open('file.txt')
str_init: str = f.read()
f.close()
str_res = ''
next = 0
i = 0
while len(str_init) > i:
    count = 0
    while str_init[i] == str_init[next]:
        count +=1
        next +=1
        if next + 1 > len(str_init):
            break
    if count == 1:
        str_res += str_init[i] + ' '
    else:
        str_res += str_init[i] + '*' + str(count) + ' '
    i = next
print(str_res)
new_f = open('new_file.txt', 'w')
new_f.write(str_res)
new_f.close()
    
