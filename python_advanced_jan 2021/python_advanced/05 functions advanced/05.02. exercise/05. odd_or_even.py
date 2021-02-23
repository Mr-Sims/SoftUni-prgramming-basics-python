command = input()

line = [int(x) for x in input().split()]

if command == "Odd":
    print(sum([x for x in line if x % 2 != 0]) * len(line))

elif command == "Even":
    print(sum([x for x in line if x % 2 == 0]) * len(line))