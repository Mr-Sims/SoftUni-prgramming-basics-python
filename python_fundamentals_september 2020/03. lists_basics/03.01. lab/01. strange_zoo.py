
list_1 = []
string_1 = list_1.append(input())
string_2 = list_1.append(input())
string_3 = list_1.append(input())

list_1[0], list_1[2] = list_1[2], list_1[0]
print(list_1)