w = float(input())
h = float(input())
3 <= h <= w <= 100
hall_pass =  1.00
true_h = h - hall_pass
work_space_w = 0.7
work_space_h = 1.2
row_work_spaces_count = true_h // work_space_w
column_work_space_count = w // work_space_h
total_work_space_count = (row_work_spaces_count * column_work_space_count) - 3
print(total_work_space_count)
