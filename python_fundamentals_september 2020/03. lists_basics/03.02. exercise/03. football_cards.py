############################ ПЪРВО РЕШЕНИЕ  ####################################################
A_team = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
B_team = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]

string_input = input()
cards_list = string_input.split()
terminated = False

for card in cards_list:
    if card in A_team:
        A_team.remove(card)
    elif card in B_team:
        B_team.remove(card)
    if len(A_team) < 7 or len(B_team) < 7:
        terminated = True
        break
print(f"Team A - {len(A_team)}; Team B - {len(B_team)}")
if terminated:
    print("Game was terminated")

######################## РЕШЕНИЕ 2 ###########################################

# a = 11
# b = 11
#
# string_input = input()
# cards_list = string_input.split()
#
# for card in range(len(cards_list)):
#     if "A" in cards_list[card]:
#         a -= 1
#         if a < 7:
#             break
#     if "B" in cards_list[card]:
#         b -= 1
#         if b < 7:
#             break
# print(f"Team A - {a}; Team B - {b}")
# if a < 7 or b < 7:
#     print("Game was terminated")

#####################   РЕШЕНИЕ Nelkata ####################################

# received_cards = input()
#
# cards_list = received_cards.split()
# A_cards = []
# B_cards = []
#
# A_team = 11
# B_team = 11
#
# is_terminated = False
#
# for item in range(len(cards_list)):
#     if cards_list[item][0] == "A":
#         if cards_list[item] in A_cards:
#             pass
#         else:
#             A_cards.append(cards_list[item])
#             A_team -= 1
#
#     if cards_list[item][0] == "B":
#         if cards_list[item] in B_cards:
#             pass
#         else:
#             B_cards.append(cards_list[item])
#             B_team -= 1
#
#     if A_team < 7 or B_team < 7:
#         is_terminated = True
#         break
#
# print(f"Team A - {A_team}; Team B - {B_team}")
# if is_terminated:
#     print(f"Game was terminated")