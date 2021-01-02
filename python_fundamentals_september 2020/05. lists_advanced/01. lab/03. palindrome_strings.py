string_list = input().split()
special_word = input()
palindrome_list = []
for el in string_list:
    rev = ""
    for i in reversed(el):
        rev += i
    if rev == el:
        palindrome_list.append(el)
print(palindrome_list)
print(f"Found palindrome {palindrome_list.count(special_word)} times")

####################### РЕШЕНИЕ ОТ LAB-A #################################

# strings = input().split(" ")
# searched_palindrome = input()
# palindromes = []
# for word in strings:
#     if word == "".join(reversed(word)):
#         palindromes.append(word)
# print(f"{palindromes}")
# print(f"Found palindrome {palindromes.count(searched_palindrome)} times")

########################### РЕШЕНИЕ ИНЕС #####################################

# string_input = input().split()
# special_word = input()
#
# palindromes = [word for word in string_input if word == word[::-1]]
# print(palindromes)
# print(f"Found palindrome {palindromes.count(special_word)}")

#######################  РЕШЕНИЕ ЙОРДАН ДЖАМБАЗОВ  #######################################


# def is_palindrome(word):
#     return word == word[::-1]
#
#
# words = input().split()
# special_palindrome = input()
# palindromes = [word for word in words if is_palindrome(word)]
# print(palindromes)
# print(f"Found palindrome {palindromes.count(special_palindrome)} times")

#######################  РЕШЕНИЕ ЙОРДАН ДЖАМБАЗОВ 2  #######################################


# words = input().split()
# special_palindrome = input()
# is_palindrome = lambda word: word == word[::-1]
# palindromes = [word for word in words if is_palindrome(word)]
# print(palindromes)
# print(f"Found palindrome {palindromes.count(special_palindrome)} times")