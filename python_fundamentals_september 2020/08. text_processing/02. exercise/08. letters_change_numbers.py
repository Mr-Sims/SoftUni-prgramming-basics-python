line = input().split()

suma = 0

for el in line:

    first_letter = el[0]
    second_letter = el[-1]
    #num = int("".join(num for num in el if num.isdigit()))
    num = int(el[1:-1:])

    if first_letter.islower():
        alphabet_num = ord(first_letter) - 96
        num *= alphabet_num
    elif first_letter.isupper():
        alphabet_num = int(ord(first_letter) - 64)
        num /= alphabet_num

    if second_letter.isupper():
        alphabet_num = int(ord(second_letter) - 64)
        num -= alphabet_num
    elif second_letter.islower():
        alphabet_num = ord(second_letter) - 96
        num += alphabet_num

    suma += num

print(f'{suma:.2f}')