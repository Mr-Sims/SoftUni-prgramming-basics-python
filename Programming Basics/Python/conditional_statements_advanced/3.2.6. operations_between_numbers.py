n1 = int(input())
n2 = int(input())
operator = input()
sum = 0
if operator == "+":
    sum = n1 + n2
elif operator == "-":
    sum = n1 - n2
elif operator == "*":
    sum = n1 * n2
elif operator == "/" and n1 != 0 and n2 != 0:
    sum = n1 / n2
elif operator == "%" and n1 != 0 and n2 != 0:
    sum = n1 % n2
if operator == "+" or operator == "-" or operator == "*":
    if sum % 2 == 0:
        print(f"{n1} {operator} {n2} = {sum} - even")
    else:
        print(f"{n1} {operator} {n2} = {sum} - odd")
elif operator == "/":
    if n1 == 0 or n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        print(f"{n1} / {n2} = {sum:.2f}")
elif operator == "%":
    if n1 == 0 or n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        print(f"{n1} % {n2} = {sum}")