ishod_spisok = [2, 9, 3, 5, 9, 3, 12, 5, 3]
multiply_simetry_el = []
n = len(ishod_spisok)
dounle_n = n
if n % 2 != 0:
    n = n // 2 + 1
else:
    n = n // 2
for i in range(n):
    multiply_simetry_el.append(ishod_spisok[i]*ishod_spisok[dounle_n-i-1])
print(multiply_simetry_el)
    
