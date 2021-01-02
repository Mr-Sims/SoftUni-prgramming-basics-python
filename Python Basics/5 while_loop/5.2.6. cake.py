# Вашата задача е да напишете програма, която изчислява броя на парчетата, които гостите са взели преди тя да свърши.
# Ще получите размерите на тортата (широчина и дължина – цели числа и след това на всеки ред, до получаване на командата "STOP" или докато не свърши тортата, броят на парчетата, които гостите вземат от нея.
# Всяко парче торта е с размер 1х1 см.
# Да се отпечата на конзолата един от следните редове:
# •	"{брой парчета} pieces are left." - ако стигнете до STOP и не са свършили парчетата торта;
# •	"No more cake left! You need {брой недостигащи парчета} pieces more."

cake_w = int(input())
cake_l = int(input())
cake_size = cake_l * cake_w
command = input()
while command != "STOP":
    cake_size -= int(command)
    if cake_size <= 0:
        print(f"No more cake left! You need {abs(cake_size)} pieces more.")
        break
    command = input()
if cake_size > 0:
    print(f"{cake_size} pieces are left.")
