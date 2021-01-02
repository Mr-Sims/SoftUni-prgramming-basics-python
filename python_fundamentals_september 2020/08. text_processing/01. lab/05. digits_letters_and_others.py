line = list(input())

digit = ""
letter = ""
symbol = ""

for el in line:
    if el.isdigit():
        digit += el
    elif el.isalpha():
        letter += el
    else:
        symbol += el
print(digit)
print(letter)
print(symbol)