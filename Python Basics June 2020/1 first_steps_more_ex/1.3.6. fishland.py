mackarel_price = float(input())
sparrowhawk_price = float(input())
bonito_kg = float(input())
horse_mackarel_kg = float(input())
mussles_kg = int(input())

bonito_price = mackarel_price * 1.6
horse_mackarel_price = sparrowhawk_price * 1.8
mussles_price = 7.5

total_price = (bonito_kg * bonito_price) + (horse_mackarel_kg * horse_mackarel_price) + (mussles_kg * mussles_price)
print(f"{(total_price):.2f}")