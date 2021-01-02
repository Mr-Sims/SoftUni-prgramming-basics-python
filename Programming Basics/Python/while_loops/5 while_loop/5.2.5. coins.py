# Производителите на вендинг машини искали да направят машините си да връщат възможно най-малко монети ресто.
# Напишете програма, която приема сума - рестото, което трябва да се върне и изчислява с колко най-малко монети може да стане това.

change = float(input())
coin_count = 0
change_coin = change * 100
while change_coin >= 1:
    if change_coin >= 200:
        change_coin -= 200
        coin_count += 1
    elif change_coin >= 100:
        change_coin -= 100
        coin_count += 1
    elif change_coin >= 50:
        change_coin -= 50
        coin_count += 1
    elif change_coin >= 20:
        change_coin -= 20
        coin_count += 1
    elif change_coin >= 10:
        change_coin -= 10
        coin_count += 1
    elif change_coin >= 5:
        change_coin -= 5
        coin_count += 1
    elif change_coin >= 2:
        change_coin -= 2
        coin_count += 1
    elif change_coin >= 1:
        change_coin -= 1
        coin_count += 1
print(coin_count)