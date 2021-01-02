n = int(input())
salary = int(input())
for i in range(0, n):
    tab = input()
    if tab == "Facebook":
        salary -= 150
    elif tab == "Instagram":
        salary -= 100
    elif tab == "Reddit":
        salary -= 50
    if salary <= 0:
        break
if salary > 0:
    print(salary)
else:
    print("You have lost your salary.")





















# n = int(input())
# salary = float(input())
# new_tab = str()
#
# for i in range(1, n+1):
#     new_tab = input()
#     if new_tab == "Facebook":
#         salary -= 150
#     elif new_tab == "Instagram":
#         salary -= 100
#     elif new_tab == "Reddit":
#         salary -= 50
#     if salary <= 0:
#         print("You have lost your salary.")
#         break
# if salary > 0:
#     print(int(salary))