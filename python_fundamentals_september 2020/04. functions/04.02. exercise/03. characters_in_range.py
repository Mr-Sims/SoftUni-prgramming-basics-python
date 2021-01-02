char_1 = input()
char_2 = input()


def char_in_range(a, b):
    res = ""
    for char in range(ord(a)+1, ord(b)):
        print(f"{chr(char)}",end=" ")
        #res += chr(char)
    return res


print(char_in_range(char_1, char_2))