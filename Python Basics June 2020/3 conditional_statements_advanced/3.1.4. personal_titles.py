age = float(input())
gender = input()

if gender == "f":
    if age < 16:
        print("Miss")
    elif age >= 16:
        print("Ms.")
elif gender == "m":
    if age < 16:
        print("Master")
    elif age >= 16:
        print("Mr.")

