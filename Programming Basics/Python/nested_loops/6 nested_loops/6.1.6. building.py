# Напишете програма, която извежда на конзолата номерата на стаите в една сграда (в низходящ ред), като са изпълнени следните условия:
# •	На всеки четен етаж има само офиси;
# •	На всеки нечетен етаж има само апартаменти;
# •	Всеки апартамент се означава по следния начин : А{номер на етажа}{номер на апартамента}, номерата на апартаментите започват от 0;
# •	Всеки офис се означава по следния начин : О{номер на етажа}{номер на офиса}, номерата на офисите също започват от 0;
# •	На последният етаж винаги има апартаменти и те са по-големи от останалите, затова пред номера им пише 'L', вместо 'А'. Ако има само един етаж, то има само големи апартаменти!
# От конзолата се прочитат две цели числа - броят на етажите и броят на стаите за един етаж.

floors_count = int(input())
rooms_count = int(input())

for floors in range(floors_count, 0, -1):

    for rooms in range(0, rooms_count):
        if floors == floors_count:  # L - Apartments
            print(f"L{floors}{rooms} ",end = "")
        elif floors % 2 == 0:                 # Offices
            print(f"O{floors}{rooms} ",end = "")
        else:                               # Apartments
            print(f"A{floors}{rooms} ",end = "")
    print()


# floors = int(input())
# rooms = int(input())
#
# for i in range(floors, 0, -1):
#     for x in range (0, rooms, + 1):
#         if floors == i:
#             print(f"L{i}{x}", end=" ")
#         elif i % 2 == 0:
#             print(f"O{i}{x}", end=" ")
#         else:
#             print(f"A{i}{x}", end=" ")
#
#     print()
