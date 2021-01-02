# От конзолата на първият ред се прочита броят на хората в журито n - цяло число.
# След това на отделен ред се прочита името на презентацията – текст.
# За всяка една презентация на нов ред се четат n - на брой оценки - реално число.
# След изчисляване на средната оценка за конкретна презентация, на конзолата се печата:
#  "{името на презентацията} - {средна оценка}."
# След получаване на команда "Finish", на конзолата се печата "Student's final assessment is {среден успех от всички презентации}." и програмата приключва.
# Всички оценки трябва да бъдат форматирани до втория знак след десетичната запетая.

jury_count = int(input())
line = input()
final_avg = 0
presentation_count = 0
while line != "Finish":
    presentation = line
    presentation_count += 1
    grade = 0
    grade_sum = 0
    for jury in range(1, jury_count + 1):
        grade = float(input())
        grade_sum += grade
    avg = grade_sum / jury_count
    final_avg += avg
    print(f"{presentation} - {avg:.2f}.")
    line = input()

print(f"Student's final assessment is {final_avg/presentation_count:.2f}.")







#
# for jury in range(1, jury_count + 1):
#     presentation = input()
#     if presentation == "Finish":
#         break
#     for grades in range(1, jury + 1):
#         grade = float(input)

