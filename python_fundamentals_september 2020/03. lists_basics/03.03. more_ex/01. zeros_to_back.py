line = input().split(", ")
zero_count = 0
result = []
for el in line:
    result.append(int(el))
    if int(el) == 0:
        result.remove(int(el))
        zero_count += 1
for count in range(zero_count):
    result.append(0)
print(result)

