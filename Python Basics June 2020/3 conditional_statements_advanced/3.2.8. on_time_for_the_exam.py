import math
exam_hour = int(input())
exam_min = int(input())
arrival_hour = int(input())
arrival_min = int(input())
exam_total_time = exam_hour * 60 + exam_min
arrival_total_time = arrival_hour * 60 + arrival_min
diff = 0
if arrival_total_time > exam_total_time:
    diff = arrival_total_time - exam_total_time
    if diff <= 59:
        print("Late")
        print(f"{diff} minutes after the start")
    if diff >= 60:
        late_hour = diff / 60
        late_min = diff % 60
        if late_min < 10:
            print("Late")
            print(f"{math.floor(late_hour)}:0{late_min}hours after the start")
        elif late_min >= 10:
            print("Late")
            print(f"{math.floor(late_hour)}:{late_min} hours after the start")
elif arrival_total_time == exam_total_time:
    print("On time")
elif arrival_total_time < exam_total_time and arrival_total_time >= exam_total_time - 30:
    diff = exam_total_time - arrival_total_time
    print("On time")
    print(f"{diff} minutes before the start")
elif arrival_total_time < exam_total_time - 30:
    diff = exam_total_time - arrival_total_time
    if diff <= 59:
        print("Early")
        print(f"{diff} minutes before the start")
    elif diff >= 60:
        early_hour = diff / 60
        early_min = diff % 60
        if early_min < 10:
            print("Early")
            print(f"{math.floor(early_hour)}:0{early_min} hours before the start")
        elif early_min >= 10:
            print("Early")
            print(f"{math.floor(early_hour)}:{early_min} hours before the start")








# hour_exam = int(input())
# minutes_exam = int(input())
# hour_coming = int(input())
# minutes_coming = int(input())
# time_difference = (hour_exam * 60 + minutes_exam) - (hour_coming * 60 + minutes_coming)
# hh = 0
# mm = 0
# if time_difference > 30:
#     if 60 <= time_difference:
#         hh = time_difference // 60
#         mm = time_difference % 60
#         if mm != 0 and mm > 9:
#             print("Early")
#             print(f"{hh}:{mm} hours before the start")
#         else:
#             print("Early")
#             print(f"{hh}:0{mm} hours before the start")
#     else:
#         print("Early")
#         print(f"{time_difference} minutes before the start")
# elif 30 >= time_difference > 0:
#     print("On time")
#     print(f"{time_difference} minutes before the start")
# elif time_difference == 0:
#     print("On time")
# else:
#     time_difference = abs(time_difference)
#     if 60 <= time_difference:
#         hh = time_difference // 60
#         mm = time_difference % 60
#         if mm != 0 and mm > 9:
#             print("Late")
#             print(f"{hh}:{mm} hours after the start")
#         else:
#             print("Late")
#             print(f"{hh}:0{mm} hours after the start")
#     else:
#         print("Late")
#         print(f"{time_difference} minutes after the start")