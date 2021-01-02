initial_string = input()
line = input()

while line != "End":
    command = line.split(" ")

    if command[0] == "Translate":
        char = command[1]
        replacement = command[2]
        initial_string = initial_string.replace(char, replacement)
        print(initial_string)

    elif command[0] == "Includes":
        string = command[1]
        if string in initial_string:
            print("True")
        else:
            print("False")

    elif command[0] == "Start":
        start_string = command[1]
        initial_string = initial_string.split(" ")
        if start_string == initial_string[0]:
            print("True")
        else:
            print("False")
        initial_string = " ".join(initial_string)

    elif command[0] == "Lowercase":
        initial_string = initial_string.lower()
        print(initial_string)

    elif command[0] == "FindIndex":
        char_to_index = command[1]
        occurances = []
        for el in range(len(initial_string)):
            if initial_string[el] == char_to_index:
                occurances.append(int(el))
        print(occurances[-1])

    elif command[0] == "Remove":
        start_index = int(command[1])
        count = int(command[2])
        stop_index = start_index + count
        initial_string = initial_string[0:start_index:] + initial_string[stop_index::]
        print(initial_string)

    line = input()