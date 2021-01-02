# Напишете програма, в която Марин решава задачи от изпити, докато не получи съобщение "Enough" от лектора си.
# При всяка решена задача той получава оценка.
# Програмата трябва да приключи прочитането на данни при команда "Enough" или ако Марин получи определения брой незадоволителни оценки. Незадоволителна е всяка оценка, която е по-малка или равна на 4.
# Изход
# •	Ако Марин стигне до командата "Enough", отпечатайте на 3 реда:
# o	"Average score: {средна оценка}"
# o	"Number of problems: {броя на всички задачи}"
# o	"Last problem: {името на последната задача}"
# •	Ако получи определеният брой незадоволителни оценки:
# o	"You need a break, {брой незадоволителни оценки} poor grades."
# Средната оценка да бъде форматирана до втория знак след десетичната запетая.

bad_grades = int(input())
bad_grades_count = 0
grades_sum = 0
average_score = 0
problem_count = 0
last_problem = 0
while bad_grades_count < bad_grades:
    problem_name = input()
    if problem_name == "Enough":
        break
    problem_count += 1
    grade = int(input())
    grades_sum += grade
    average_score = grades_sum / problem_count
    if grade <= 4:
        bad_grades_count += 1
    last_problem = problem_name
if bad_grades_count >= bad_grades:
    print(f"You need a break, {bad_grades_count} poor grades.")
else:
    print(f"Average score: {average_score:.2f}\nNumber of problems: {problem_count}\nLast problem: {last_problem}")