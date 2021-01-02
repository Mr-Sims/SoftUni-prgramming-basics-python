n = int(input())
list_1 = []
word = input()

for el in range(0, n):
    line = input()
    list_1.append(line)
print(list_1)

for el in range(len(list_1)-1, -1, -1):
    element = list_1[el]
    if word not in element:
        list_1.remove(element)
print(list_1)