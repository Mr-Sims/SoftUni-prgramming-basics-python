n = int(input())
sum_num = 0
for i in range(1, n+1):
    num = int(input())
    sum_num += num
print(f"{(sum_num/n):.2f}")