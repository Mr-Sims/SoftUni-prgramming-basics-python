###########################################
###
line = input()
vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']
res = [el for el in line if el not in vowels]
print(''.join(res))

###########################################
### with upper/lower
line = input()
vowels = ['a', 'o', 'u', 'e', 'i']
res = [el for el in line if el.lower() not in vowels]

print(''.join(res))

#############################################
#######

line = input()
vowels = {'a', 'o', 'u', 'e', 'i'}
vowels = vowels.union(x.upper() for x in vowels)
res = [el for el in line if el not in vowels]
print(''.join(res))
