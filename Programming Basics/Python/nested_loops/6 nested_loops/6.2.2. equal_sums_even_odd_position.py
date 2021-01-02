num1 = int(input())
num2 = int(input())

for i in range(num1, num2 + 1):
    num_as_string = str(i)
    even = 0
    odd = 0
    for index, symbol in enumerate(num_as_string):

        if index % 2 == 0:
            even += int(symbol)
        else:
            odd += int(symbol)
    if even == odd:
        print(i, end=" ")