from math import ceil
from math import floor
magnolias_count = int(input())
zumbiul_count = int(input())
roses_count = int(input())
cacti_count = int(input())
gift_price = float(input())
tax = 0.95
sale = ((magnolias_count * 3.25) + (zumbiul_count * 4) + (roses_count * 3.5) + (cacti_count * 8)) * tax
if sale >= gift_price:
    print(f"She is left with {floor(sale - gift_price)} leva.")
else:
    print(f"She will have to borrow {ceil(gift_price - sale)} leva.")
