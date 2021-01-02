# Напишете програма, която чете от конзолата цели числа, докато не се получи команда "stop".
# Да се намери сумата на всички въведени прости и сумата на всички въведени непрости числа.
# Тъй като по дефиниция от математиката отрицателните числа не могат да бъдат прости,
# ако на входа се подаде отрицателно число, да се изведе следното съобщение "Number is negative.".
# В този случай въведено число се игнорира и не се прибавя към нито една от двете суми, а програмата продължава своето изпълнение, очаквайки въвеждане на следващо число.
# На изхода да се отпечатат на два реда двете намерени суми в следния формат:
# "Sum of all prime numbers is: {prime numbers sum}"
# "Sum of all non prime numbers is: {nonprime numbers sum}"

line = input()
prime = 0
non_prime = 0
while line != "stop":
    num = int(line)
    if num >= 0:
        for i in range(2, num):
            if (num % i) == 0:
                non_prime += num
                break
        else:
            prime += num
    else:
        print("Number is negative.")
    line = input()
print(f"Sum of all prime numbers is: {prime}")
print(f"Sum of all non prime numbers is: {non_prime}")

# ЧУЖДО РЕШЕНИЕ

line = input()
prime_sum = 0
not_prime_sum = 0

while line != 'stop':
    number = int(line)
    if number < 0:
        print("Number is negative.")
    else:
        counter = 0
        for i in range(1, number + 1):
            if number % i == 0:
                counter += 1
        if counter == 2 or number == 1:
            prime_sum += number
        else:
            not_prime_sum += number
    line = input()
print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {not_prime_sum}")


