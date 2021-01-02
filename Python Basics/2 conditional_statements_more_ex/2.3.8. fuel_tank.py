# Ако литрите гориво са повече или равни на 25, на конзолата да се отпечата "You have enough {вида на горивото}.",
# ако са по-малко от 25, да се отпечата "Fill your tank with {вида на горивото}!".
# В случай, че бъде въведено гориво, различно от посоченото, да се отпечата "Invalid fuel!".

fuel_type = input() #"Diesel", "Gasoline" или "Gas"
fuel_amount = float(input())
if fuel_type == "Diesel":
    if fuel_amount >= 25:
        print(f"You have enough diesel.")
    else:
        print(f"Fill your tank with diesel!")
elif fuel_type == "Gasoline":
    if fuel_amount >= 25:
        print(f"You have enough gasoline.")
    else:
        print(f"Fill your tank with gasoline!")
elif fuel_type == "Gas":
    if fuel_amount >= 25:
        print(f"You have enough gas.")
    else:
        print(f"Fill your tank with gas!")
else:
    print("Invalid fuel!")