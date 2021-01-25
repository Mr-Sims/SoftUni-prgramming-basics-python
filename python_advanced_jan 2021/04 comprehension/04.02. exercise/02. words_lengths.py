###########################################################################
###########################################################################
#### dict comprehenion with funcs

def find_len():
    return {word: len(word) for word in input().split(", ")}


def generate_result_list():
    return [f"{key} -> {value}" for key, value in find_len().items()]


def print_result():
    print(", ".join(generate_result_list()))


print_result()

###########################################################################
###########################################################################
##### list comprehension

res = [f"{name} -> {len(name)}" for name in input().split(", ")]
print(", ".join(res))

###########################################################################
###########################################################################
##### list comprehension v2

line = input().split(", ")
print(*[f"{word} -> {len(word)}" for word in line], sep=", ")

###########################################################################
###########################################################################
##### full oneliner list comprehension

print(", ".join([f"{name} -> {len(name)}" for name in input().split(", ")]))


