data = list(input())

my_dict = {}

for el in data:
    if el == " ":
        continue
    if el not in my_dict:
        my_dict[el] = 0
    my_dict[el] += 1

for key, value in my_dict.items():
    print(f"{key} -> {value}")


