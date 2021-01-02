n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for i in range(1, n + 1):
    num = int(input())
    if num < 200:
        p1 += 1
    elif 200 <= num <= 399:
        p2 += 1
    elif 400 <= num <= 599:
        p3 += 1
    elif 600 <= num <= 799:
        p4 += 1
    elif num >= 800:
        p5 += 1
print(f"{((p1/n)*100):.2f}%")
print(f"{((p2/n)*100):.2f}%")
print(f"{((p3/n)*100):.2f}%")
print(f"{((p4/n)*100):.2f}%")
print(f"{((p5/n)*100):.2f}%")




























# n = int(input())
# new_num = int()
# p1, p2, p3, p4, p5 = (0, 0, 0, 0, 0)
#
# for i in range(1, n+1):
#     new_num = int(input())
#     if new_num < 200 :
#         p1 += 1
#     elif 200 <= new_num < 400:
#         p2 += 1
#     elif 400 <= new_num < 600:
#         p3 += 1
#     elif 600 <= new_num < 800:
#         p4 += 1
#     else:
#         p5 += 1
#
# print(f"{(p1/n*100):.2f}%")
# print(f"{(p2/n*100):.2f}%")
# print(f"{(p3/n*100):.2f}%")
# print(f"{(p4/n*100):.2f}%")
# print(f"{(p5/n*100):.2f}%")
#
#
#
# #############################################
# n =int(input())
#
# p1 = 0
# p2 = 0
# p3 = 0
# p4 = 0
# p5 = 0
#
# for i in range(1, n+1):
#     number = int(input())
#     if number < 200:
#         p1 += 1
#     elif 200 <= number <= 399:
#         p2 += 1
#     elif 400 <= number <= 599:
#         p3 += 1
#     elif 600 <= number <= 799:
#         p4 += 1
#     else:
#         p5 += 1
# print(f"{p1 / n * 100:.2f}%")
# print(f"{p2 / n * 100:.2f}%")
# print(f"{p3 / n * 100:.2f}%")
# print(f"{p4 / n * 100:.2f}%")
# print(f"{p5 / n * 100:.2f}%")