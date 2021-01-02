tax = 1.2
special = 0.9
current_sum = 0

while True:
    line = input()
    if line == "special" or line == "regular":
        break
    if float(line) < 0:
        print("Invalid price!")
    else:
        current_sum += float(line)

if current_sum <= 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {current_sum:.2f}$\n"
          f"Taxes: {current_sum * tax - current_sum:.2f}$\n"
          f"-----------")
    if line == "special":
        print(f"Total price: {current_sum * tax * special:.2f}$")
    else:
        print(f"Total price: {current_sum * tax:.2f}$")