number_entries = int(input())
students_log = {}

for entry in range(number_entries):
    name = input()
    grade = float(input())
    if name in students_log:
        students_log[name].append(grade)
        av_grade = sum(students_log[name]) / len(students_log[name])
        students_log[name] = av_grade
    elif name not in students_log:
        students_log[name] = []
        students_log[name].append(grade)

for key, value in students_log.items():
    if isinstance(value, list):
        av_grade = sum(students_log[key]) / len(students_log[key])
        students_log[key] = av_grade

sort_by_grade = dict(sorted(students_log.items(),reverse=True, key=lambda x: x[1]))

for key, value in sort_by_grade.items():
    if value < 4.5:
        continue
    else:
        print(f"{key} -> {value:.2f}")