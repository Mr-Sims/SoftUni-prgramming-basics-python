budget = float(input())
season = input()
destination = ""
vacation_type = ""
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        budget *= 0.3
        vacation_type = "Camp"
    elif season == "winter":
        budget *= 0.7
        vacation_type = "Hotel"
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        vacation_type = "Camp"
        budget *= 0.4
    elif season == "winter":
        budget *= 0.8
        vacation_type = "Hotel"
elif budget > 1000 and (season == "summer" or season == "winter"):
    destination = "Europe"
    budget *= 0.9
    vacation_type = "Hotel"
print(f"Somewhere in {destination}")
print(f"{vacation_type} - {budget:.2f}")
