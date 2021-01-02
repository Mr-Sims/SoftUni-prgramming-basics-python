secret_message = input().split()
deciphered = []
for el in secret_message:
    nums = [int(symbol) for index, symbol in enumerate(list(el)) if symbol.isdigit()]
    letters = [symbol for index, symbol in enumerate(list(el)) if not symbol.isdigit()]
    letters[0], letters[-1] = letters[-1], letters[0]
    deciphered.append(chr(int(''.join(map(str,nums)))) + "".join(letters))
print(" ".join(deciphered))
