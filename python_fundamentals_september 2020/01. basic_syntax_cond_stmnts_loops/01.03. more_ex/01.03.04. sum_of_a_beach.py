#####################################################################################
#############################  МОЕ РЕШЕНИЕ - 100/100 ########################################################
string = input().lower()

a = [i for i in range(len(string)) if string.startswith('sun', i)]
b = [i for i in range(len(string)) if string.startswith('fish', i)]
c = [i for i in range(len(string)) if string.startswith('sand', i)]
d = [i for i in range(len(string)) if string.startswith('water', i)]
print(len(a) + len(b) + len(c) + len(d))





################   Ч У Ж Д О    Р Е Ш Е Н И Е    #################
string = input()
string_lower = string.lower()
keywords = ['sand', 'water', 'fish', 'sun']
count = 0

for keyword in keywords:
    count += string_lower.count(keyword)

print(count)


################   Ч У Ж Д О    Р Е Ш Е Н И Е    #################
word_snake = input()

word_matches = ["water", "sand", "sun", "fish"]
match = 0

for i in range(len(word_matches)):
    match += word_snake.lower().count(word_matches[i])

print(match)

################   Ч У Ж Д О    Р Е Ш Е Н И Е    #################

# s = input().casefold()
# n = 0
# last = ''
# for i in range(len(s)):
#     last += s[i]
#     if i > 1:
#         test = ''
#         for j in range(4, 0, -1):
#             test += last[len(last) - j]
#         if test == 'sand':
#             n += 1
#         test = ''
#         for j in range(5, 0, -1):
#             test += last[len(last) - j]
#         if test == 'water':
#             n += 1
#         test = ''
#         for j in range(4, 0, -1):
#             test += last[len(last) - j]
#         if test == 'fish':
#             n += 1
#         test = ''
#         for j in range(3, 0, -1):
#             test += last[len(last) - j]
#         if test == 'sun':
#             n += 1
# print(n)