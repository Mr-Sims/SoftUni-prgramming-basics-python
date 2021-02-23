###################################################################################
############ dictionary solution ################################################
line = list(input())
occurrences = {}

for i in line:
    if i not in occurrences:
        occurrences[i] = 1
    else:
        occurrences[i] += 1

sorted_dict = dict(sorted(occurrences.items(), key=lambda x: x[0]))
for key, value in sorted_dict.items():
    print(f"{key}: {value} time/s")
