line = input()
vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']
res = [el for el in line if el not in vowels]
print(''.join(res))
# res = ""
# for i in line:
#     if i not in vowels:
#         res += i


