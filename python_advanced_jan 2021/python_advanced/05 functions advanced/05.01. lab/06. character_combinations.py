################################################################
###############################################################
# Ines solution

def permutate(text, current_index=0):
    if current_index == len(text):
        print("".join(text))
        return

    for i in range(current_index, len(text)):
        text[current_index], text[i] = text[i], text[current_index]
        permutate(text, current_index + 1)
        text[current_index], text[i] = text[i], text[current_index]


text = list(input())
permutate(text)


################################################################
###############################################################
# lab imported alg solution

from itertools import permutations

text = input()
per = list(permutations(text))

print(*[f"{''.join(el)}" for el in per], sep="\n")

################################################################
###############################################################
# lab solution

def print_comb(text, idx):
    if idx >= len(text):
        print("".join(text))
        return
    print_comb(text, idx + 1)
    for i in range(idx + 1, len(text)):
        text[idx], text[i] = text[i], text[idx]
        print_comb(text, idx + 1)
        text[idx], text[i] = text[i], text[idx]

text = list(input())
print_comb(text, 0)
