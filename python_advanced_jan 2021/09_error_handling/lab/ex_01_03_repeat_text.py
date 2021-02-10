text = input()
try:
    n_times_to_repeat = int(input())

    res = ""
    for repeat in range(n_times_to_repeat):
        res += text
    print(res)
except:
    print("Variable times must be an integer")

#############################################################################3
### lab solution

try:
    text = input()
    times = int(input())
    print(text * times)

except ValueError:
    print("Variable times must be an integer")

#############################################################################3
### lab solution v2


def repeat_text(text, count):
    return text * int(count)


text = input()
count = input()

try:
    print(repeat_text(text, count))
except ValueError:
    print("Variable times must be an integer")