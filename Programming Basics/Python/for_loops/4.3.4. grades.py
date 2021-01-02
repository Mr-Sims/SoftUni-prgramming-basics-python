# Напишете програма, която да пресмята статистика на оценки от изпит.
# В началото програмата получава броят на студентите явили се на изпита и за всеки студент неговата оценка.
# На края програмата трябва да изпечата процента на студенти с оценка
# между 2.00 и 2.99,
# между 3.00 и 3.99,
# между 4.00 и 4.99,
# 5.00 или повече.
# Също така и средният успех на изпита.
# Изход
# Да се отпечатат на конзолата 5 реда, които съдържат следната информация:
# Ред 1 -	"Top students: {процент студенти с успех 5.00 или повече}%"
# Ред 2 -	"Between 4.00 and 4.99: {между 4.00 и 4.99 включително}%"
# Ред 3 -	"Between 3.00 and 3.99: {между 3.00 и 3.99 включително}%"
# Ред 4 -	"Fail: {по-малко от 3.00}%"
# Ред 5 -	"Average: {среден успех}"

students_count = int(input())
top = 0
good = 0
acceptable = 0
fail = 0
total_grades = 0
for students in range(1, students_count + 1):
    grade = float(input())
    if grade >= 5:
        top += 1
        total_grades += grade
    elif 4 <= grade <= 4.99:
        good += 1
        total_grades += grade
    elif 3 <= grade <= 3.99:
        acceptable += 1
        total_grades += grade
    elif grade < 3:
        fail += 1
        total_grades += grade
print(f"Top students: {(top / students_count) * 100:.2f}%")
print(f"Between 4.00 and 4.99: {(good / students_count) * 100:.2f}%")
print(f"Between 3.00 and 3.99: {(acceptable / students_count) * 100:.2f}%")
print(f"Fail: {(fail / students_count) * 100:.2f}%")
print(f"Average: {total_grades / students_count:.2f}")
