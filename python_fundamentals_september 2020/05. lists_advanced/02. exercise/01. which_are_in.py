substrings = input().split(", ")
full_strings = input().split(", ")
initial = [el for el in substrings for ele in full_strings if el in ele]
print(sorted(set(initial), key=initial.index))




# for el in substrings:
#     for ele in full_strings:
#         if el in ele and el not in filtered:
#             filtered.append(el)
