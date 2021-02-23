numbers_list = [int(el) for el in input().split(", ")]
result = 1
for number in numbers_list:
    if number <= 5:
        result *= number
    elif 5 < number <= 10:
        result /= number
print(result)
