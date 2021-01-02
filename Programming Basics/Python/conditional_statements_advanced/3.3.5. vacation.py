budget = float(input())
season = input()
sum = 0
location = ""
stay = ""
if budget <= 1000:
    if season == "Summer":
        location = "Alaska"
        stay = "Camp"
        sum = budget * 0.65
        print(f"{location} - {stay} - {sum:.2f}")
    elif season == "Winter":
        location = "Morocco"
        stay = "Camp"
        sum = budget * 0.45
        print(f"{location} - {stay} - {sum:.2f}")
elif 1000 < budget <= 3000:
    if season == "Summer":
        location = "Alaska"
        stay = "Hut"
        sum = budget * 0.80
        print(f"{location} - {stay} - {sum:.2f}")
    elif season == "Winter":
        location = "Morocco"
        stay = "Hut"
        sum = budget * 0.60
        print(f"{location} - {stay} - {sum:.2f}")
elif budget > 3000:
    if season == "Summer":
        location = "Alaska"
        stay = "Hotel"
        sum = budget * 0.90
        print(f"{location} - {stay} - {sum:.2f}")
    elif season == "Winter":
        location = "Morocco"
        stay = "Hotel"
        sum = budget * 0.90
        print(f"{location} - {stay} - {sum:.2f}")
