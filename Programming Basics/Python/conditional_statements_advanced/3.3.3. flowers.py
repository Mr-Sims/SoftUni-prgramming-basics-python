hrizantema_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = input()
day = input()
sum = 0
if season == "Spring" or season == "Summer":
    if day == "Y":
        sum = (hrizantema_count * 2 + roses_count * 4.1 + tulips_count * 2.5) * 1.15
    elif day == "N":
        sum = hrizantema_count * 2 + roses_count * 4.1 + tulips_count * 2.5
elif season == "Autumn" or season == "Winter":
    if day == "Y":
        sum = ((hrizantema_count * 3.75 + roses_count * 4.5 + tulips_count * 4.15) * 1.15)
    if day == "N":
        sum = (hrizantema_count * 3.75 + roses_count * 4.5 + tulips_count * 4.15)
if season == "Spring" and tulips_count > 7:
    sum *= 0.95
if season == "Winter" and roses_count >= 10:
    sum *= 0.9
if (hrizantema_count + roses_count + tulips_count) > 20:
    sum *= 0.8
boquete = sum + 2
print(f"{boquete:.2f}")
