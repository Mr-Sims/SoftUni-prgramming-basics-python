time_span = int(input())
doctors = 7
treated = 0
untreated = 0
for days in range(1, time_span+1):
    patients_per_day = int(input())
    if days % 3 == 0 and untreated > treated:
        doctors += 1
    if patients_per_day <= doctors:
        treated += patients_per_day
        untreated += 0
    else:
        treated += doctors
        untreated += patients_per_day - doctors
print(f"Treated patients: {treated}.")
print(f"Untreated patients: {untreated}.")