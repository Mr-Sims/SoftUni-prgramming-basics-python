################################################################################
#####################  МОЕ РЕШЕНИЕ ##########################################
import re
sentence = input().lower()
word = input().lower()
pattern = r"((?<=^)|(?<=\s))"+word+"($|(?=\s)|(?=\.)|(?=\,)|(?=\?)|(?=\!))"

#pattern = fr"((?<=^)|(?<=\s)){word}($|(?=\s)|(?=\.)|(?=\,)|(?=\?)|(?=\!))"

matches = [el.group() for el in re.finditer(pattern, sentence)]
print(len(matches))

##################################################################################
##############################  ИНЕС  ###############################################33

# import re
# line = input()
# word = input()
#
# pattern = f"\\b{word}\\b"
#
# matches = re.findall(pattern, line, re.IGNORECASE)
#
# print(len(matches))
