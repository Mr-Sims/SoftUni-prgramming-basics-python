####################################################

n = int(input())

record = {}

for i in range(n):
    student, grade = input().split(" ")
    if student not in record:
        record[student] = []
    record[student].append(float(grade))

for student, grades in record.items():
    #print(f"{student} -> {' '.join(map(lambda grade: f'{grade:.2f}', grades))} (avg: {float(sum(grades) / len(grades)):.2f})")
    print(f"{student} -> {' '.join([f'{grade:.2f}' for grade in grades])} (avg: {float(sum(grades) / len(grades)):.2f})")
################################# lab #####################################################################################

# count = int(input())
# students = {}
# for _ in range(count):
#     line = input().split()
#     student = line[0]
#     grade = float(line[1])
#     if student not in students:
#         students[student] = [grade]
#     else:
#         students[student].append(grade)
#
# for student, grade in students.items():
#     average = float(sum(grade) / len(grade))
#     print(f"{student} -> {' '.join(map(lambda grade: f'{grade:.2f}', grades))} (avg: {average:.2f})")


###############################  solution Doncho #######################################################

# def input_to_list(count):
#     lines = []
#     for _ in range(count):
#         lines.append(input())
#
#     return lines
#
#
# n = int(input())
# students_grades_lines = input_to_list(n)
#
#
# def avg(values):
#     return sum(values) / len(values)
#
# students_grades = {}
#
#
# for line in students_grades_lines:
#     student, grade = line.split(" ")
#     if student not in students_grades:
#         students_grades[student] = []
#     students_grades[student].append(float(grade))
#
# for student, grades in students_grades.items():
#     grades_string = ' '.join(map(lambda grade: f'{grade:.2f}', grades))
#     avg_grade = avg(grades)
#     print(f"{student} -> {grades_string} (avg: {avg_grade:.2f})")








