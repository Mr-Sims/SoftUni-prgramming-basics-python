# Вашата задача е да напишете програма, която да изчислява
# процента на билетите за всеки тип от продадените билети:
# студентски(student),
# стандартен(standard) и
# детски(kid),
# за всички прожекции.
# Трябва да изчислите и колко процента от залата е запълнена за всяка една прожекция.
# Вход

# Входът е поредица от цели числа и текст:
# •	На първия ред до получаване на командата "Finish" - име на филма – текст
# •	На втори ред – свободните места в салона за всяка прожекция – цяло число [1 … 100]
# •	За всеки филм, се чете по един ред до изчерпване на свободните места в залата или до получаване на командата "End":
# o	Типа на закупения билет - текст ("student", "standard", "kid")

# МОЕ РЕШЕНИЕ

movie = input()
student = 0
standard = 0
kid = 0
total_tickets = 0
current_movie_tickets = 0
while movie != "Finish":
    free_seats = int(input())
    line = input()
    while line != "End":
        ticket_type = str(line)
        if ticket_type == "student":
            student += 1
        elif ticket_type == "standard":
            standard += 1
        elif ticket_type == "kid":
            kid += 1
        current_movie_tickets += 1
        total_tickets += 1
        if current_movie_tickets >= free_seats:
            break
        else:
            line = input()
    print(f"{movie} - {(current_movie_tickets / free_seats) * 100:.2f}% full.")
    current_movie_tickets = 0
    movie = input()
print(f"Total tickets: {total_tickets}")
print(f"{(student / total_tickets) * 100:.2f}% student tickets.")
print(f"{(standard / total_tickets) * 100:.2f}% standard tickets.")
print(f"{(kid / total_tickets) * 100:.2f}% kids tickets.")


# ЧУЖДО РЕШЕНИЕ
# line = input()
# standard_ticket = 0
# student_ticket = 0
# kid_ticket = 0
# total_sold_tickets = 0
# while line != "Finish":
#     free_sits = int(input())
#     full_sits = 0
#     while full_sits < free_sits:
#         type_ticket = input()
#         if type_ticket == 'standard':
#             standard_ticket += 1
#         elif type_ticket == 'student':
#             student_ticket += 1
#         elif type_ticket == 'kid':
#             kid_ticket += 1
#         if type_ticket == 'End':
#             break
#         full_sits += 1
#         total_sold_tickets += 1
#     print(f'{line} - {full_sits / free_sits * 100:.2f}% full.')
#     line = input()
# print(f'Total tickets: {total_sold_tickets}')
# print(f'{student_ticket / total_sold_tickets * 100:.2f}% student tickets.')
# print(f'{standard_ticket / total_sold_tickets * 100:.2f}% standard tickets.')
# print(f'{kid_ticket / total_sold_tickets * 100:.2f}% kids tickets.')