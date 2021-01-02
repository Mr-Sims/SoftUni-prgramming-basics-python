n = int(input())
odd = 0
even = 0
for i in range(1, n + 1):
    num = int(input())
    if i % 2 == 0:
        even += num
    else:
        odd += num
if even == odd:
    print(f"Yes\nSum = {even}")
else:
    print(f"No\nDiff = {abs(even - odd)}")

