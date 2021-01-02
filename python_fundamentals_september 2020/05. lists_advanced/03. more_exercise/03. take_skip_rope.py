string = list(input())

digits = [int(el) for el in string if el.isdigit()]
string = [el for el in string if not el.isdigit()]

take = [int(x) for index, x in enumerate(digits) if index % 2 == 0]
skip = [int(x) for index, x in enumerate(digits) if index % 2 != 0]
res = ""
while len(string):
    for el in take:
        res += "".join(string[:el:])
        del string[:el:]
        take.pop(0)
        break
    for sk in skip:
        del string[:sk:]
        skip.pop(0)
        break
print(res)
