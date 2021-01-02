budget = float(input())
season = input()
rent = 0
if budget <= 100:
    if season == "Summer":
        rent = budget * 0.35
        print("Economy class")
        print(f"Cabrio - {rent:.2f}")
    elif season == "Winter":
        rent = budget * 0.65
        print("Economy class")
        print(f"Jeep - {rent:.2f}")
elif 100 < budget <= 500:
    if season == "Summer":
        rent = budget * 0.45
        print("Compact class")
        print(f"Cabrio - {rent:.2f}")
    elif season == "Winter":
        rent = budget * 0.8
        print("Compact class")
        print(f"Jeep - {rent:.2f}")
elif budget > 500:
    if season == "Summer" or season == "Winter":
        rent = budget * 0.9
        print("Luxury class")
        print(f"Jeep - {rent:.2f}")
