
letter_c_has_appeared = False
letter_o_has_appeared = False
letter_n_has_appeared = False

message = ""
current_word = ""
while True:

    if letter_c_has_appeared and letter_o_has_appeared and letter_n_has_appeared:
        message += current_word + " "
        current_word = ""
        letter_c_has_appeared = False
        letter_o_has_appeared = False
        letter_n_has_appeared = False
    line = input()

    if line == "End":
        break

    letter = ord(line)

    if not (65 <= letter <= 90 or 97 <= letter <= 122):
        continue

    if line == "c" and not letter_c_has_appeared:
        letter_c_has_appeared = True
        continue
    if line == "o" and not letter_o_has_appeared:
        letter_o_has_appeared = True
        continue
    if line == "n" and not letter_n_has_appeared:
        letter_n_has_appeared = True
        continue

    current_word += line

print(message)

