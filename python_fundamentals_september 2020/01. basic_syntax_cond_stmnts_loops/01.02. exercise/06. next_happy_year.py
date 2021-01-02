# You're saying good-bye to your best friend, "See you next happy year".
# Happy Year is the year with only distinct digits, (e.g) 2018.
# Write a program that receives an integer number and finds the next happy year.

# year = int(input())
# happy_year = 0
# year_is_found = False
# for i in range(0, 9+1):
#     if year_is_found:
#         break
#     for j in range(0, 9+1):
#         if year_is_found:
#             break
#         for k in range(0, 9+1):
#             if year_is_found:
#                 break
#             for l in range(0, 9+1):
#                 if l != k and l != j and l !=i and k != j and k != i and j != i:
#                     happy_year = int(f"{i}{j}{k}{l}")
#                     if happy_year > year:
#                         print(happy_year)
#                         year_is_found = True
#                         break

# РЕШЕНИЕ СЛАВИ КАПСАЛОВ

year = input()
year_as_int = int(year) +1
year = str(year_as_int)

while True:
    symbols_count = len(year)
    unique_count = len(set(year))

    if symbols_count == unique_count:
        break
    else:
        year_as_int += 1
        year = str(year_as_int)
print(year)