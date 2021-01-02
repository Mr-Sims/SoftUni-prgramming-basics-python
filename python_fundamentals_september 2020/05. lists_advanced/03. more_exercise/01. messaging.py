nums_list = [el for el in input().split()]
string = list(input())
message = ""
for i in nums_list:
    n = [int(el) for el in i]
    index = sum(n)
    if index > len(string):
        index -= len(string)

    message += string.pop(index)
print(message)