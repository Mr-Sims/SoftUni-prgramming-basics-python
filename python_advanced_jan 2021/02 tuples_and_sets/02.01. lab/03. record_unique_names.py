# n = int(input())
# names = []
# for _ in range(n):
#     names.append(input())
#
# for person in set(names):
#     print(person)

####################################################################################################


n = int(input())
unique_names = set()
for i in range(n):
    unique_names.add(input())
for person in unique_names:
    print(person)
