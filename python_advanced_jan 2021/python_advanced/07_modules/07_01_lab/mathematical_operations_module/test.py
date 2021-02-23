from mathematical_operations_module.calculate import calculate_nums

line = input().split(" ")
x = float(line[0])
operator = str(line[1])
y = int(line[2])

calculate_nums(x, y, operator)