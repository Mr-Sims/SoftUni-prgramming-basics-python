vacation = float(input())
puzzles = int(input())
dolls = int(input())
teddies = int(input())
minnions = int(input())
trucks = int(input())
profit = (puzzles * 2.6 + dolls * 3 + teddies * 4.1 + minnions * 8.2 + trucks * 2) * 0.9
toys_count = puzzles + dolls + teddies + minnions + trucks

if toys_count >= 50:
    profit = profit * 0.75
profit_net = profit - vacation
if profit >= vacation:
    print(f"Yes! {profit_net:.2f} lv left.")
elif profit < vacation:
    profit_net = vacation - profit
    print(f"Not enough money! {(profit_net):.2f} lv needed.")