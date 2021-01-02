# inputs_count = int(input())
#
# synonyms = {}
#
# for inp in range(inputs_count):
#     key = input()
#     value = input()
#     if key in synonyms:
#         synonyms[key] += f", {value}"
#     else:
#         synonyms[key] = value
#
# for key, value in synonyms.items():
#     print(f"{key} - {value}")

####################################################################################
##############################################################################


inputs_count = int(input())

synonyms = {}

for inp in range(inputs_count):
    key = input()
    value = input()
    if key in synonyms:
        synonyms[key].append(value)
    else:
        synonyms[key] = [value]

for key, value in synonyms.items():
    print(f"{key} - {', '.join(value)}")