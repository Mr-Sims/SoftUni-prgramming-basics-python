month = input()
nights_count = int(input())
studio = 0
apartment = 0
if month == "May" or month == "October":
    studio = 50
    apartment = 65
    if 7 < nights_count <= 14:
        studio *= 0.95
    elif nights_count > 14:
        studio *= 0.7
        apartment *= 0.9
elif month == "June" or month == "September":
    studio = 75.2
    apartment = 68.7
    if nights_count > 14:
        studio *= 0.8
        apartment *= 0.9
elif month == "July" or month == "August":
    studio = 76
    apartment = 77
    if nights_count > 14:
        apartment *= 0.9
print(f"Apartment: {(nights_count * apartment):.2f} lv.")
print(f"Studio: {(nights_count * studio):.2f} lv.")


# monat = input()
# night_count = int(input())
# studio = 0
# apartment = 0
# if monat == "May" or monat == "October":
#     studio = 50
#     apartment = 65
#     if 7 < night_count <= 14:
#         studio = studio * 0.95
#     elif night_count > 14:
#         studio = studio * 0.70
#         apartment = apartment * 0.90
# elif monat == "June" or monat == "September":
#     studio = 75.20
#     apartment = 68.70
#     if night_count > 14:
#         studio = studio * 0.80
#         apartment = apartment * 0.90
# else:
#     studio = 76
#     apartment = 77
#     if night_count > 14:
#         apartment = apartment * 0.90
# print(f"Apartment: {(night_count * apartment):.2f} lv.")
# print(f"Studio: {(night_count * studio):.2f} lv.")