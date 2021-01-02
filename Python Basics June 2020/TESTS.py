line = input()

prime_sum = 0
non_prime_sum = 0

while line != "stop":
    counter = 0
    num = int(line)
    if num > 0:
        for i in range(1, num+1):
            if num % i == 0:
                counter += 1
                if counter > 2:
                    break
        if counter == 2 or num == 1:
            prime_sum += num
        else:
            non_prime_sum += num
    elif num == 0:
        non_prime_sum += num
    else:
        print("Number is negative.")
    line = input()
print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")


