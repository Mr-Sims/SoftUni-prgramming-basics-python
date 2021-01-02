# Given a string, you have to print a string in which each character (case-sensitive) is repeated.
#
# Hello World  -	HHeelllloo  WWoorrlldd
#
# 1234! -	11223344!!

word = input()

for i in word:
    print(i * 2, end="")