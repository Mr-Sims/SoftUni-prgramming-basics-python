# line_one = input().split()
# line_two = input().split()
# line_three = input().split()
#
# first_player_won = False
# second_player_won = False
#
# if line_one[0] == line_one[1] == line_one[2]:
#     if line_one[0] == "1":
#         first_player_won = True
#     elif line_one[0] == "2":
#         second_player_won = True
#
# elif line_two[0] == line_two[1] == line_two[2]:
#     if line_two[0] == "1":
#         first_player_won = True
#     elif line_two[0] == "2":
#         second_player_won = True
#
# elif line_three[0] == line_three[1] == line_three[2]:
#     if line_three[0] == "1":
#         first_player_won = True
#     elif line_three[0] == "2":
#         second_player_won = True
# elif line_one[0] == line_two[0] == line_three[0]:
#     if line_one[0] == "1":
#         first_player_won = True
#     elif line_one[0] == "2":
#         second_player_won = True
#
# elif line_one[1] == line_two[1] == line_three[1]:
#     if line_one[1] == "1":
#         first_player_won = True
#     elif line_one[1] == "2":
#         second_player_won = True
#
# elif line_one[2] == line_two[2] == line_three[2]:
#     if line_one[2] == "1":
#         first_player_won = True
#     elif line_one[2] == "2":
#         second_player_won = True
#
# elif line_one[0] == line_two[1] == line_three[2]:
#     if line_one[0] == "1":
#         first_player_won = True
#     elif line_one[0] == "2":
#         second_player_won = True
#
# elif line_one[2] == line_two[1] == line_three[0]:
#     if line_one[2] == "1":
#         first_player_won = True
#     elif line_one[2] == "2":
#         second_player_won = True
#
#
# if first_player_won:
#     print("First player won")
# elif second_player_won:
#     print("Second player won")
# else:
#     print("Draw!")
#

############################################################################



line_one = input().split()
line_two = input().split()
line_three = input().split()


def check(a, b, c):
    if a == b == c and a == "1":
        return 1


    else:
        pass


print(check(line_one[0], line_one[1], line_one[2]))
print(check(line_two[0], line_two[1], line_two[2]))
print(check(line_three[0], line_three[1], line_three[2]))

print(check(line_one[0], line_two[0], line_three[0]))
print(check(line_one[1], line_two[1], line_three[1]))
print(check(line_one[2], line_two[2], line_three[2]))

print(check(line_one[0], line_two[1], line_three[2]))
print(check(line_one[2], line_two[1], line_three[0]))
# else:
#     print("Draw!")