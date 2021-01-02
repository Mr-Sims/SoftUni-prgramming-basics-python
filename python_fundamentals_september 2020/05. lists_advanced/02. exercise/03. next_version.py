# current_ver = [int(el) for el in input().split(".")]
# a = current_ver[0]
# b = current_ver[1]
# c = current_ver[2]+1
# if c == 10:
#     c = 0
#     b += 1
#     if b == 10:
#         b = 0
#         a += 1
# next_version = str(a) + str(b) + str(c)
# result = ".".join(next_version)
# print(result)

##################################################################333
#################### Климентина ###############################################

current_version = input().split(".")
new = int("".join(current_version))
new_version = int(new+1)
print(".".join(str(new_version)))