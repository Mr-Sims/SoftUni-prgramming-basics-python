

def loading_bar(a):
    work_num = a / 10

    loading_digits = ""
    rest_digits = ""
    for i in range(1, int(work_num) + 1):
        loading_digits = i * "%"
    rest_digits_num = 10 - work_num
    for j in range(1, int(rest_digits_num) + 1):
        rest_digits = j * "."
    loading_b = f"[{loading_digits}{rest_digits}]"
    if a == 100:
        return f"{a}% Complete!\n{loading_b}"
    else:
        return f"{a}% {loading_b}\nStill loading..."


num = int(input())
print(loading_bar(num))