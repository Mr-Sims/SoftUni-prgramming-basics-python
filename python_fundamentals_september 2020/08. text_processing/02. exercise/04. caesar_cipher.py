# string = input()
# res = ""
# for letter in string:
#     res += chr(ord(letter)+3)
# print(res)

#############################################################

string = list(input())
res = [chr(ord(el)+3) for el in string]
print("".join(res))
