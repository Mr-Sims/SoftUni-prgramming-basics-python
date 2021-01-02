tank_capacity = 255
n = int(input())
fullness = 0

for i in range(0, n):
    new_amount = int(input())
    fullness += new_amount
    if tank_capacity < fullness:
        print("Insufficient capacity!")
        fullness -= new_amount
print(fullness)
