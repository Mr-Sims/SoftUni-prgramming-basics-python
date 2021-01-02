# Напишете програма, която генерира и принтира на конзолата четирицифрени числа,
# в които първата и втората двойка цифри образуват двуцифрени прости числа (пример за такова число 1723).
# Крайната стойност до която трябва да се генерират двойките се определя от други 2 цифри,
# подадени като вход, които определят с колко крайната стойност е по-голяма от началната.

# Изход:
# Да се отпечатат на конзолата четирицифрените числа, в които първите две и вторите две цифри са прости двуцифрени числа.

num1 = int(input())
num2 = int(input())
first_pair_diff = int(input())
second_pair_diff = int(input())

for i in range(num1, 100):
    for j in range(num2, 100):
        if (i == 2 or i == 3 or i == 5 or i == 7 or i == 11 or i == 13 or i == 17 or i == 19 or i == 23 or i == 29 or i == 31 or i == 37 or i == 41 or i == 43 or i == 47 or i == 53 or i == 59 or i == 61 or i == 67 or i == 71 or i == 73 or i == 79 or i == 83 or i == 89 or i == 97 or i == 101) and (j == 2 or j == 3 or j == 5 or j == 7 or j == 11 or j == 13 or j == 17 or j == 19 or j == 23 or j == 29 or j == 31 or j == 37 or j == 41 or j == 43 or j == 47 or j == 53 or j == 59 or j == 61 or j == 67 or j == 71 or j == 73 or j == 79 or j == 83 or j == 89 or j == 97 or j == 101) and i <= num1 + first_pair_diff and j <= num2 + second_pair_diff:
            print(f"{i}{j}")



