n = int(input())

set_elements = set()

for i in range(n):

    line = input().split()
    for j in range(len(line)):
        set_elements.add(line[j])

for _ in set_elements:
    print(_)