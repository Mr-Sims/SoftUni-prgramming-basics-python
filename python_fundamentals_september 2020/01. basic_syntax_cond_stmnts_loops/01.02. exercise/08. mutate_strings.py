
############ МОЕ РЕШЕНИЕ 1 - 60/100 #####################
string_1 = input()
string_2 = input()

new_word = ""
new_word_2 = ""
final = ""
final_2 = ""
string_1_list = list(string_1)
string_2_list = list(string_2)

for i in range(len(string_1)):
    for j in string_1:
        new_word += j
        string_1_list.remove(j)
        string_1 = "".join(string_1_list)
        break
    for k in string_2:
        new_word_2 += k
        string_2_list.remove(k)
        string_2 = "".join(string_2_list)
        break
    final = new_word_2 + string_1
    if final == final_2:
        pass
    else:
        print(final)
    final_2 = final


############################# # ЧУЖДO РЕШЕНИЯ  ###############################################
#
# input_string = input()
# output_string = input()
# s = input_string
#
# for i in range(len(input_string)):
#     s1 = input_string[(i + 1):]
#     s2 = output_string[:(i + 1)]
#     if s2 + s1 == s:
#         continue
#     s = s2 + s1
#     print(s)
#
############################### МОЕ РЕШЕНИЕ 2 - работещо ###################


string_one = list(input())
string_two = list(input())
new_string = ""

while len(string_one):
    new_string_one = ""
    new_string_two = ""

    for i in string_one:
        new_string_one += i
        string_one.remove(i)
        break

    for j in string_two:
        new_string_two += j
        string_two.remove(j)
        break
    if new_string_one != new_string_two:
        new_string += new_string_two
        print(new_string + "".join(string_one))
    else:
        new_string += new_string_one