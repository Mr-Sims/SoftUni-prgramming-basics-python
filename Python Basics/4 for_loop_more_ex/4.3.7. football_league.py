# Екипът на СофтУни си организира футболен турнир.
# Първоначално прочитаме от конзолата капацитета на стадиона и броят на всички фенове.
# След това за всеки фен се чете секторът, в който се намира.
# Феновете на първия отбор са в сектор А и Б, а на втория – В и Г.
# Да се напише програма, която изчислява процентите на феновете във всеки сектор,
# спрямо общия брой фенове на стадиона,
# както и общият процент на феновете за двата отбора, спрямо капацитета на стадиона.
# Общият брой на феновете НЕ надвишава капацитета на стадиона.

stadium_capacity = int(input())
fans_count = int(input())
a_count = 0
b_count = 0
v_count = 0
g_count = 0
for fans in range(1, fans_count+1):
    stadium_sector = input()  # "A", "B", "V" и "G".
    if stadium_sector == "A":
        a_count += 1
    elif stadium_sector == "B":
        b_count += 1
    elif stadium_sector == "V":
        v_count += 1
    elif stadium_sector == "G":
        g_count += 1
print(f"{(a_count/fans_count)*100:.2f}%")
print(f"{(b_count/fans_count)*100:.2f}%")
print(f"{(v_count/fans_count)*100:.2f}%")
print(f"{(g_count/fans_count)*100:.2f}%")
print(f"{(fans_count/stadium_capacity)*100:.2f}%")
