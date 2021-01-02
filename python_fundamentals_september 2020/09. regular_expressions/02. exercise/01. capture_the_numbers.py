# import re
# pattern = r"\d+"
# line = input()
# string = ""
#
# while line:
#     string += line+", "
#     line = input()
# matches = re.findall(pattern, string)
#
# print(*matches)


###########  ИНЕС


import re

nums = []
line = input()
pattern = r"\d+"

while line:
   match = re.findall(pattern, line)
   nums.extend(match)

   line = input()

print(*nums)
