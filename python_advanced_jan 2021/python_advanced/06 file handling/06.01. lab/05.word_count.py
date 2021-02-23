import re


def write_result(res):
    with open("output.txt", "w") as file:
        file.writelines("\n".join(res))


def get_file_content(path_to_file):
    with open(path_to_file, "r") as file:
        text = "".join(file.readlines())
        return re.findall(r"[a-zA-Z']+", text.lower())


path_to_words = "words.txt"
path_to_text = "text_1.txt"

first_file = get_file_content(path_to_words)
seconds_file_words = get_file_content(path_to_text)

analyse = {}

for word in first_file:
    if word in seconds_file_words:
        analyse[word] = seconds_file_words.count(word)

result = [f"{el[0]} - {el[1]}" for el in sorted(analyse.items(), key=lambda x: -x[1])]
write_result(result)