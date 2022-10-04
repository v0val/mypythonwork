ishod_spisok = [2.01, 9.34, 3.123, 5.97, 9.65, 3, 12.3, 5.1, 3.27]
print(ishod_spisok)
fract_part = []
for i in range(len(ishod_spisok)):
    fract_part.append(round(ishod_spisok[i] - int(ishod_spisok[i]), 3))
print(fract_part)
print(max(fract_part) - min(fract_part))

