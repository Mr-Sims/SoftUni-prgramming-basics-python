def even_odd(*args):
    command = args[-1]
    if command == "even":
        nums = [int(x) for x in args[:-1] if x % 2 == 0]
        return nums

    elif command == "odd":
        nums = [int(x) for x in args[:-1] if x % 2 != 0]
        return nums


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))