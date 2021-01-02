import sys
n = input()
v = -sys.maxsize
while n != "Stop":
    num = int(n)
    if num > v:
        v = num
    n = input()
print(v)