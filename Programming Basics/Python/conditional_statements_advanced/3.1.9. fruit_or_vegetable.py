# Да се напише програма, която чете име на продукт, въведено от потребителя, и проверява дали е плод или зеленчук.
# •	Плодовете "fruit" имат следните възможни стойности:  banana, apple, kiwi, cherry, lemon и grapes;
# •	Зеленчуците "vegetable" имат следните възможни стойности:  tomato, cucumber, pepper и carrot;
# •	Всички останали са "unknown".
# Да се изведе "fruit", "vegetable" или "unknown" според въведения продукт.

# A TOMATO IS ACTUALLY A FRUIT!!!! DON`T YOU KNOW ANYTHING?!?!? :D
zarzavat = str(input())

if zarzavat == "banana" or zarzavat == "apple" or zarzavat == "kiwi" or zarzavat == "cherry" or zarzavat == "lemon" or zarzavat == "grapes":
    print("fruit")
elif zarzavat == "tomato" or zarzavat == "cucumber" or zarzavat == "pepper" or zarzavat == "carrot":
    print("vegetable")
else:
    print("unknown")
