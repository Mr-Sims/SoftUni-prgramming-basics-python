# Поздравления, поради вашите задълбочени знания в сферата на програмирането МВР реши да наеме точно вас за създаването на новата им система за генериране на специални автомобилни номера. Всеки един специален автомобилен номер се състой от четири числа. Условията, които разграничават специалните от обикновените номера са следните:
# •	Ако номерът започва с четна цифра, то той трябва да завършва на нечетна цифра и обратното – ако започва с нечетна,  завършва на четна
# •	Първата цифра от номера е по-голяма от последната
# •	Сумата от втората и третата цифра трябва да е четно число
# Входа се състой от две числа - начало и край на интервал, между които трябва да се генерира всяко едно число от номера.

n1 = int(input())
n2 = int(input())

for i in range(n1, n2 + 1):
    for j in range(n1, n2 + 1):
        for k in range(n1, n2 + 1):
            for l in range(n1, n2 + 1):
                if ((i % 2 == 0 and l % 2 == 1) or (i % 2 == 1 and l % 2 == 0)) and (i > l) and ((j + k) % 2 == 0):
                    print(f"{i}{j}{k}{l}", end=" ")


