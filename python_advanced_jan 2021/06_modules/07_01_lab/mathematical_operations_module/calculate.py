def calculate_nums(x, y, operator):
    result = 0
    if operator == "/":
        result =  x / y
    elif operator == "*":
        result =  x * y
    elif operator == "-":
        result = x - y
    elif operator == "+":
        result = x + y
    elif operator == "^":
        result = x ** y
    print(f"{result:.2f}")