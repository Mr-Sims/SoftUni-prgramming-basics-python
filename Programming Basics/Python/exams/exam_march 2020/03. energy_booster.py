fruit = input() #1.	Плод - текст с възможности: "Watermelon", "Mango", "Pineapple" или "Raspberry
set_size = input() #2.	Размерът на сета - текст с възможности: "small" или "big"
count = int(input())#3.	Брой на поръчаните сетове - цяло число

if set_size == "small":
    if fruit == "Watermelon":
        price = 56 * 2
    elif fruit == "Mango":
        price = 36.66 * 2
    elif fruit == "Pineapple":
        price = 42.1 * 2
    elif fruit == "Raspberry":
        price = 20 * 2
elif set_size == "big":
    if fruit == "Watermelon":
        price = 28.7 * 5
    elif fruit == "Mango":
        price = 19.6 * 5
    elif fruit == "Pineapple":
        price = 24.8 * 5
    elif fruit == "Raspberry":
        price = 15.2 * 5
total = price * count
if 400 <= total <= 1000:
    total  *= 0.85
elif total > 1000:
    total *= 0.5
print(f"{total:.2f} lv.")