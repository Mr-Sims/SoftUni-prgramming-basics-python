# Напишете програма, която да отпечатва часовете в денонощието от 0:0:0 до 23:59:59, всеки на отделен ред.
# Часовете да се изписват във формат "{час} : {минути} : {секунди} ".
#
#

hour = 0
min = 0
sec = 0
while hour <= 23:
    while min < 60:
         while sec < 60:
            print(f"{hour} : {min} : {sec}")
            sec += 1
         min += 1
         sec = 0
         continue
    hour += 1
    min = 0
    sec = 0
    continue
