# Да се напише програма която чете ден от седмицата (текст) – въведен от потребителя и принтира на конзолата цената на билет за кино според деня от седмицата:

day = str(input())

if day == "Monday" or day == "Tuesday" or day == "Friday":
    print("12")
elif day == "Wednesday" or day == "Thursday":
    print("14")
elif day == "Saturday" or day == "Sunday":
    print("16")
