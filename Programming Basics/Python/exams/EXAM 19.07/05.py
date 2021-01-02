max_goals = 0
best_player = ""
hat_trick = False
line = input()
while line != "END":
    goals_scored = int(input())
    if goals_scored > max_goals:
        max_goals = goals_scored
        best_player = line
        if goals_scored >= 3:
            hat_trick = True
    if goals_scored >= 10:
        break
    line = input()
print(f"{best_player} is the best player!")
if hat_trick:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")