# Kids drink toddy, Teens drink coke, Young adults drink beer, Adults drink whisky.
# Make a program that receives an age, and returns what they drink.
# Rules:
# Kids under 14 years old.
# Teens under 18 years old.
# Young adults under 21 years old.
# Adults above 21.
# Note: All the values except the last one are inclusive!

age = int(input())
drink = ""
if age <= 14:
    drink = "toddy"
elif age <= 18:
    drink = "coke"
elif age <= 21:
    drink = "beer"
elif age > 21:
    drink = "whisky"
print(f"drink {drink}")
#############################################
# age = int(input())
# message = "drink "
# if age <= 14:
#     message += "toddy"
# elif age <= 18:
#     message += "coke"
# elif age <= 21:
#     message += "beer"
# else:
#     message += "whisky"
# print(message)