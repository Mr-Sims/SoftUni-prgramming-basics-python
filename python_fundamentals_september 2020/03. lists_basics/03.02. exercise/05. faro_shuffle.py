deck = input()
shuffle = int(input())
deck_list = deck.split()
half_deck = int(len(deck_list) / 2)
deck_1 = []
deck_2 = []

for shuffle in range(shuffle):
    while len(deck_list) > half_deck:
        deck_1.append(deck_list[0])
        deck_list.pop(0)
    deck_2 = deck_list
    deck_list = []
    for i in range(half_deck):
        deck_list.append(deck_1[0])
        deck_1.pop(0)
        deck_list.append(deck_2[0])
        deck_2.pop(0)

print(deck_list)


#################### ЧУЖДО РЕШЕНИЕ със .zip()  #########################################

# deck = input().split()
# number_shuffles = int(input())
# half = len(deck) // 2
#
# for i in range(number_shuffles):
#
#     current_shuffle = zip(
#         deck[:half], deck[half:]
#     )
#
#     deck.clear()
#
#     for pair in current_shuffle:
#         deck.extend(pair)
#
# print(deck)