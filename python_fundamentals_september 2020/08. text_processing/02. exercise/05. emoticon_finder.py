line = input()
for el in range(len(line)):
    if line[el] == ":":
        print(line[el]+line[el+1])


# line = input()
# for index in range(len(line)):
#     if line[index] == ":":
#         print(line[index:index + 2])