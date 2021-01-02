line = input().split()
string_1, string_2 = line
suma = 0
if len(string_1) > len(string_2):
    for i in range(len(string_1)):
        if i >= len(string_2):
            suma += ord(string_1[i])
        else:
            suma += ord(string_2[i]) * ord(string_1[i])

elif len(string_1) < len(string_2):
    for i in range(len(string_2)):
        if i >= len(string_1):
            suma += ord(string_2[i])
        else:
            suma += ord(string_1[i]) * ord(string_2[i])
else:
    for i in range(len(string_1)):
        suma += ord(string_1[i]) * ord(string_2[i])
print(suma)
