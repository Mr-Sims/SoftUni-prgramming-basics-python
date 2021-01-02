party_size = int(input())
days = int(input())
earnings = 50 * days


for day in range(1, days + 1):

    if day % 10 == 0:
        party_size -= 2
    if day % 15 == 0:
        party_size += 5

    earnings -= party_size * 2

    if day % 3 == 0:
        earnings -= party_size * 3
    if day % 5 == 0:
        earnings += party_size * 20
        if day % 3 == 0:
            earnings -= party_size * 2

earnings_per_member = int(earnings / party_size)
print(f"{party_size} companions received {earnings_per_member} coins each.")