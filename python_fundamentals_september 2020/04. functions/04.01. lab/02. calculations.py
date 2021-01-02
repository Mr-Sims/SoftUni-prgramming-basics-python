input_operator = input()
num_1 = int(input())
num_2 = int(input())


def solve(a, b, operator):
    result = None
    if operator == "multiply":
        result = a * b
    elif operator == "divide":
        result = a / b
    elif operator == "add":
        result = a + b
    elif operator == "subtract":
        result = a - b
    return int(result)


print(solve(num_1, num_2, input_operator))