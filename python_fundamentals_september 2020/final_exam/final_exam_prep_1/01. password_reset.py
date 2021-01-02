def take_odd(raw_pass):
    result = ""
    for index in range(1, len(raw_pass), 2):
        result += raw_pass[index]
    print(result)
    return result


def cut(raw_pass, i, length):
    result = raw_pass[:i] + raw_pass[i+length:]
    print(result)
    return result


def substitute(raw_pass, sub_str, repl):
    result = raw_pass.replace(sub_str, repl)
    if result == raw_pass:
        print("Nothing to replace!")
    else:
        print(result)
    return result


password = input()
line = input()

while not line == "Done":
    data = line.split(' ')
    command = data[0]
    if command == "TakeOdd":
        password = take_odd(password)
    elif command == "Cut":
        index, length = [int(el) for el in data[1:]]
        password = cut(password, index, length)
    elif command == "Substitute":
        sub_str, replacement = data[1:]
        password = substitute(password, sub_str, replacement)
    line = input()

print(f"Your password is: {password}")

###########################################################################################


password = input()

def take_odd_action(old_pass):
    new_pass = ""
    for i in range(len(old_pass)):
        if i % 2 == 1:
            new_pass += old_pass[i]
    return new_pass

def cut_action(old_pass, cut_index, length_index):
    cut_chars = old_pass[cut_index:cut_index+length_index]
    new_pass = old_pass.replace(cut_chars, "", 1)
    return new_pass

def substitute_action(old_pass, old_char, new_char):
    if old_char in old_pass:
        new_pass = old_pass.replace(old_char, new_char)
        return new_pass


while True:
    command = input()
    if command == "Done":
        break

    txt = command.split(" ")

    if txt[0] == "TakeOdd":
        password = take_odd_action(password)
        print(password)
    elif txt[0] == "Cut":
        index = int(txt[1])
        length = int(txt[2])
        password = cut_action(password, index, length)
        print(password)
    elif txt[0] == "Substitute":
        substring = txt[1]
        substitute = txt[2]
        if substring in password:
            password = substitute_action(password, substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

print(f"Your password is: {password}")

#############################################################################################

raw_password = input()
command = input()



while not command == "Done":
    command = command.split()
    typ = command[0]

    if typ == "TakeOdd":
        every_second_char = [el for el in raw_password[1::2]]
        raw_password = ""
        raw_password = ''.join(every_second_char)
        print(raw_password)
    elif typ == "Cut":
        index = int(command[1])
        length = index + int(command[2])
        as_list = list(raw_password)
        del as_list[index:length]
        raw_password = ''.join(as_list)
        print(raw_password)
    elif typ == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in raw_password:
            raw_password = raw_password.replace(substring, substitute)
            print(raw_password)
        else:
            print("Nothing to replace!")
    command = input()


print(f"Your password is: {raw_password}")