# Напишете програма, която отпечатва часовете в денонощието от 0:0 до 23:59,
# всеки на отделен ред. Часовете трябва да се изписват във формат "{час} : {минути}".

hour = 0
min = 0

while hour <= 23:
    while min < 60:
        print(f"{hour} : {min}")
        min +=1
    hour += 1
    min = 0
    continue
