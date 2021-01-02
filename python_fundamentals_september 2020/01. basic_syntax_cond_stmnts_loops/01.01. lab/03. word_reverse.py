# word = input()
# reverse_word = ""
# for i in range(len(word)-1, -1, -1):
#     reverse_word += word[i]
# print(reverse_word)

##################
# word = input()
# for i in range(len(word)-1, -1, -1):
#     print(word[i], end= "")

word = input()

reversed_word = ""

for i in reversed(word):
    reversed_word += i
print(reversed_word)