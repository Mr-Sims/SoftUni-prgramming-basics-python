# Катерачи от цяла България се събират на групи и набелязват следващите върхове за изкачване. Според размера на групата, катерачите ще изкачват различни върхове.
# •	Група до 5 човека– Мусала
# •	Група от 6 до 12 – Монблан
# •	Група от 13 до 25 – Килиманджаро
# •	Група от 26 до 40 – К2
# •	Група от 41 или повече – Еверест
# Да се напише програма, която изчислява процента на катерачите изкачващи всеки връх.

groups_count = int(input())
musala_group = 0
montblanc_group = 0
kilimandjaro_group = 0
k2_group = 0
everest_group = 0
total_count = 0
for i in range(1, groups_count + 1):
    ppl_per_group = int(input())
    total_count += ppl_per_group
    if ppl_per_group <= 5:
        musala_group += ppl_per_group
    elif 6 <= ppl_per_group <= 12:
        montblanc_group += ppl_per_group
    elif 13 <= ppl_per_group <= 25:
        kilimandjaro_group += ppl_per_group
    elif 26 <= ppl_per_group <= 40:
        k2_group += ppl_per_group
    elif ppl_per_group >= 41:
        everest_group += ppl_per_group

print(f"{(musala_group / total_count) * 100:.2f}%")
print(f"{(montblanc_group / total_count) * 100:.2f}%")
print(f"{(kilimandjaro_group / total_count) * 100:.2f}%")
print(f"{(k2_group / total_count) * 100:.2f}%")
print(f"{(everest_group / total_count) * 100:.2f}%")




# Изход
# Да се отпечатат на конзолата 5 реда, всеки от които съдържа процент между 0.00% и 100.00%.
# •	Първи ред - процентът изкачващи Мусала
# •	Втори ред – процентът изкачващи Монблан
# •	Трети ред – процентът изкачващи Килиманджаро
# •	Четвърти ред – процентът изкачващи К2
# •	Пети ред – процентът изкачващи Еверест
# Резултатът да се форматира до втория знак след десетичната запетая.
