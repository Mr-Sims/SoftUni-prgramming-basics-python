class ValueCannotBeNegative(Exception):
    """Number is below zero"""
    pass


for i in range(5):
    number = int(input())
    if number < 0:
        raise ValueCannotBeNegative


############################################################################
##### lab demo
# class ValueCannotBeNegativeError(Exception):
#     def __init__(self, value):
#         super().__init__(f"{value} is negative")
#
#
# def validate_positive_numbers(numbesr):
#     for number in numbers:
#         if number < 0:
#             raise ValueCannotBeNegativeError(number)
#
#
#
# numbers = [1, 2, -1, 4, 5]
# validate_positive_numbers(numbers)
# print("Numbers are positive")