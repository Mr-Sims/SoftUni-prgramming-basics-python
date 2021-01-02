import re

pattern = r"(\+359\s2\s\d{3} \d{4}|\+359-2-\d{3}-\d{4}\b)"
text = input()

match = re.findall(pattern, text)

print(", ".join(match))

###################################################################
########################### Инес #########################################
#
# import re
# data = input()
# pattern = r"(\+359\s2\s\d{3} \d{4})|(\+359-2-\d{3}-\d{4}\b)"
# phones = re.finditer(pattern, data)
# phones = [p.group(0) for p in phones]
# print(", ".join(phones))


