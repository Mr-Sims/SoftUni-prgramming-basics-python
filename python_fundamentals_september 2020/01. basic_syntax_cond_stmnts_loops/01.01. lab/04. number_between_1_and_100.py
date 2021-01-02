# while True:
#     number = float(input())
#     if 1 <= number <= 100:
#         print(f"The number {number} is between 1 and 100")
#         break


#####

num = float(input())
while num < 1 or num > 100:
    num = float(input())
print(f"The number {num} is between 1 and 100")