# •	До 3 тона – микробус (200 лева на тон)
# •	От 4 до 11 тона – камион (175 лева на тон)
# •	12 и повече тона – влак (120 лева на тон)
# Вашата задача е да изчислите средната цена на тон превозен товар,
# както и процента на тоновете  превозвани с всяко превозно средство,
# спрямо общото тегло(в тонове) на всички товари.
# Изход
# Да се отпечатат на конзолата 4 реда, както следва:
# •	Първи ред – средната цена на тон превозен товар (закръглена до втория знак след дес. запетая);
# •	Втори ред – процентът тона превозвани с микробус (процент между 0.00% и 100.00%);
# •	Трети ред – процентът  тона превозвани с камион (процент между 0.00% и 100.00%);
# •	Четвърти ред – процентът тона превозвани с влак (процент между 0.00% и 100.00%).

loads_count = int(input())
total_weight = 0
bus = 0
truck = 0
train = 0
for loads in range(1, loads_count + 1):
    load_weight = int(input())
    if load_weight <= 3:
        bus += load_weight
        total_weight += load_weight
    elif 4 <= load_weight <= 11:
        truck += load_weight
        total_weight += load_weight
    elif load_weight >= 12:
        train += load_weight
        total_weight += load_weight
avg = ((bus * 200) + (truck * 175) + (train * 120)) / total_weight
bus_percent = (bus / total_weight) * 100
truck_percent = (truck / total_weight) * 100
train_percent = (train / total_weight) * 100
print(f"{avg:.2f}")
print(f"{bus_percent:.2f}%")
print(f"{truck_percent:.2f}%")
print(f"{train_percent:.2f}%")
