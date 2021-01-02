fourcebook = {}

while True:

    line = input()
    if line == "Lumpawaroo":
        break

    if " | " in line:
        a = line.split(" | ")
        side = a[0]
        jedi = a[1]

        if side not in fourcebook:
            fourcebook[side] = []
            fourcebook[side].append(jedi)
        elif side in fourcebook:
            if jedi in fourcebook[side]:
                continue
            else:
                fourcebook[side].append(jedi)


    elif " -> " in line:
        b = line.split(" -> ")
        side = b[1]
        jedi = b[0]

        for key, value in fourcebook.items():
            if jedi in value:
                fourcebook[key].remove(jedi)

        if side not in fourcebook:
            fourcebook[side] = []
            fourcebook[side].append(jedi)
        else:
            fourcebook[side].append(jedi)
            print(f"{jedi} joins the {side} side!")

if len(fourcebook.keys()) == len(set(fourcebook.keys())):
    sort = dict(sorted(fourcebook.items(), key=lambda x: x[0]))
else:
    sort = dict(sorted(fourcebook.items(),reverse=True, key=lambda x: len(x[0])))


for key, value in sort.items():
    if len(sort[key]) == 0:
        continue
    else:
        print(f"Side: {key}, Members: {len(sort[key])}")
    for value in sorted(sort[key]):
        print(f"! {value}")