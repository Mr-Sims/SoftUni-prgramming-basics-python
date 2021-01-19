n = int(input())
intersections_list = []

for i in range(n):
    line = input().split("-")
    first = line[0].split(",")
    first_start = int(first[0])
    first_stop = int(first[1])

    second = line[1].split(",")
    second_start = int(second[0])
    second_stop = int(second[1])
    set_1 = set()
    set_2 = set()
    for j in range(first_start, first_stop+1):
        set_1.add(j)

    for k in range(second_start, second_stop+1):
        set_2.add(k)
    intersections_list.append(set_1 & set_2)
maxed = 0
longest = 0
for leng in range(len(intersections_list)):
    if len(intersections_list[leng]) > maxed:
        maxed = len(intersections_list[leng])
        longest = leng
longest_intersection = list(intersections_list[longest])

print(f"Longest intersection is {longest_intersection} with length {maxed}")