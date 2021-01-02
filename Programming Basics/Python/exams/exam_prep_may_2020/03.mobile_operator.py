contract_term = input()
contract_type = input()
additional_net = input()
months = int(input())
price_per_month = 0
if contract_term == "one":
    if contract_type == "Small":
        price_per_month = 9.98
    elif contract_type == "Middle":
        price_per_month = 18.99
    elif contract_type == "Large":
        price_per_month = 25.98
    elif contract_type == "ExtraLarge":
        price_per_month = 35.99
elif contract_term == "two":
    if contract_type == "Small":
        price_per_month = 8.58
    elif contract_type == "Middle":
        price_per_month = 17.09
    elif contract_type == "Large":
        price_per_month = 23.59
    elif contract_type == "ExtraLarge":
        price_per_month = 31.79
if additional_net == "yes":
    if price_per_month <= 10:
        price_per_month += 5.5
    elif 11 <= price_per_month <= 30:
        price_per_month += 4.35
    elif price_per_month > 30:
        price_per_month += 3.85
total = months * price_per_month
if contract_term == "two":
    total *= 0.9625
print(f"{total:.2f} lv.")