count_list = [int(el) for el in input().split(" ")]

n = count_list[0]
m = count_list[1]


set_n = set()
set_m = set()


for _ in range(n):
    set_n.add(int(input()))

for _ in range(m):
    set_m.add(int(input()))

final = set_n & set_m

for i in final:
    print(i)