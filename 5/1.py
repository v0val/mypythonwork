str1 = 'ваидл драбвал карабд страбв \n абку совба соабвку абв старбв колбав'

print(str1)

str_to_mas = str1.split()
print(str_to_mas)

new_mas =[x for x in str_to_mas if not('абв' in x)]
str1 = ' '.join(new_mas)

print(str1)
