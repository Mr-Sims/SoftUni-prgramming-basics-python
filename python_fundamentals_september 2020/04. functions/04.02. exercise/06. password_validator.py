CHAR_RANGE_LOWER = range(97, 123)
CHAR_RANGE_UPPER = range(65, 91)
CHAR_RANGE_DIGIT = range(48, 58)

str = input()


def valid_password(a):
    lenght_is_valid = True
    let_digit_valid = True
    min_digit_valid = True
    if not 6 <= len(a) <= 10:
        lenght_is_valid = False
    for el in a:
        if not ord(el) in CHAR_RANGE_DIGIT and not ord(el) in CHAR_RANGE_LOWER and not ord(el) in CHAR_RANGE_UPPER:
            let_digit_valid = False
    digit_counter = 0
    for digit in a:
        if ord(digit) in CHAR_RANGE_DIGIT:
            digit_counter += 1
    if digit_counter < 2:
        min_digit_valid = False
    if lenght_is_valid and let_digit_valid and min_digit_valid:
        print("Password is valid")
    if not lenght_is_valid:
        print("Password must be between 6 and 10 characters")
    if not let_digit_valid:
        print("Password must consist only of letters and digits")
    if not min_digit_valid:
        print("Password must have at least 2 digits")


valid_password(str)
