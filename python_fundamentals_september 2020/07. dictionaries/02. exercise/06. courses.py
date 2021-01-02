courses = {}

while True:
    line = input().split(" : ")

    if line[0] == 'end':
        break

    course = line[0]
    student = line[1]
    if course in courses:
        courses[course].append(student)
    elif course not in courses:
        courses[course] = []
        courses[course].append(student)

sort_by_count = dict(sorted(courses.items(), reverse=True, key=lambda x: (len(x[1]))))

for key, value in sort_by_count.items():
    print(f"{key}: {len(value)}")
    sort_by_student_name = sorted(value)
    for name in sort_by_student_name:
        print(f"-- {name}")