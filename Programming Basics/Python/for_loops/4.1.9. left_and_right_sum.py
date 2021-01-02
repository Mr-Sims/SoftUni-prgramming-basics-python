n = int(input())
left = 0
right = 0
for i in range(n):
    num = int(input())
    left += num
for i in range(n):
    num = int(input())
    right += num

if left == right:
    print(f"Yes, sum = {left}")
else:
    print(f"No, diff = {abs(left - right)}")
