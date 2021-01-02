name = input()
grade = 1
total_score = 0.0
bad_score = 0
while grade <= 12:
    score = float(input())
    if score < 4:
        bad_score += 1
        if bad_score == 2:
            break
        continue
    total_score += score
    grade += 1
if bad_score == 2:
    print(f"{name} has been excluded at {grade} grade")
else:
    grade -= 1
    print(f"{name} graduated. Average grade: {(total_score / grade):.2f}")
