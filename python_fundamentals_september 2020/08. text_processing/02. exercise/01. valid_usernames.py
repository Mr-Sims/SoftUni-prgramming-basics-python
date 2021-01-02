line = input().split(", ")
valid = []
for name in line:
    if 3 <= len(name) <= 16:
        counter = 0
        for el in name:
            if el.isdigit() or el.isalpha() or el == "-" or el == "_":
                counter += 1
                if counter == len(name):
                    valid.append(name)
            else:
                break
for el in valid:
    print(el)