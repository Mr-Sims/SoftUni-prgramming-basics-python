# num = int(input())
#
# if 100 <= num <= 200 and num == 0:
#     print("y")
# else:
#     print("invalid")

number = int(input())
is_valid = 100 <= number <= 200 or number == 0

if not is_valid:
    print("invalid")
