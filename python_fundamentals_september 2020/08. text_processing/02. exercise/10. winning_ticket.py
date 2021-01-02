line = input().split(', ')
winning_symbols = ['@', '$', '#', '^']


def jackpot(ticket):
    left = ticket[0:10]
    right = ticket[10:20]
    if not left == right:
        return False
    for symbol in winning_symbols:
        if symbol * 20 == ticket:
            print(f'ticket "{ticket}" - 10{symbol} Jackpot!')
            return True
    return False


def winning_ticket(ticket):
    left = ticket[0:10]
    right = ticket[10:20]
    for symbol in winning_symbols:
        if symbol * 6 in left and symbol*6 in right:
            count_left = left.count(symbol)
            count_right = right.count(symbol)
            count = min(count_left, count_right)
            print(f'ticket "{ticket}" - {count}{symbol}')
            return True
    return False


for t in line:
    ticket = t.strip()
    if not len(ticket) == 20:
        print('invalid ticket')
        continue
    if jackpot(ticket):
        continue
    if winning_ticket(ticket):
        continue
    print(f'ticket "{ticket}" - no match')


