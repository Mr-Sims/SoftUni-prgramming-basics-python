str = input()
repeat_count = int(input())

def repeat_string(string, count):
    res = ""
    for repeat in range(count):
        res += string
    return res


print(repeat_string(str, repeat_count))
