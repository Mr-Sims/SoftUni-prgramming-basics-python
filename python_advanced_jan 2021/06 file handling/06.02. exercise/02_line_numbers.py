import re


def get_n(line, path_regex):
    return len(re.findall(path_regex, line))


def write_result(res):
    with open("output.txt", "w") as file:
        file.writelines("\n".join(res))


letter_path = r"[a-zA-Z]"
path_punctuation = r"[-,\.\!\?']"
result = []
with open("text.txt", "r") as file:
    lines = file.readlines()
    counter = 1
    for line in lines:
        n_letter = get_n(line, letter_path)
        n_punctuations = get_n(line, path_punctuation)
        result.append(f"Line {counter}: {line[:-1]} ({n_letter})({n_punctuations})")
        counter += 1

write_result(result)