import re
##################################################################
############### Решение Инес ################################
# data = input()
#
# pattern = r"\d{2}([\./-])[A-Z][a-z]{2}\1\d{4}"
#
# dates = re.finditer(pattern, data)
#
# for date in dates:
#     m_object = date.group(0)
#     day = m_object[0:2]
#     month = m_object[3:6]
#     year = m_object[7:11]
#     print(f"Day: {day}, Month: {month}, Year: {year}")

#######################################################################################3
############## Решение от LAB-a с регекс от Инес

# data = input()
# pattern = r"(?P<day>\d{2})(?P<delimiter>[\./-])(?P<month>[A-Z][a-z]{2})(?P=delimiter)(?P<year>\d{4})"  # може и да не се слагат имена на групите. Не е задължително за конкретния код
# matches = re.findall(pattern, data)
# for match in matches:
#     print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")

#######################################################################################3
############## Решение Инес с речници $##################################

data = input()
pattern = r"(?P<day>\d{2})(?P<delimiter>[\./-])(?P<month>[A-Z][a-z]{2})(?P=delimiter)(?P<year>\d{4})"

dates = re.finditer(pattern, data)

for date in dates:
    d = date.groupdict()
    print(f"Day: {d['day']}, Month: {d['month']}, Year: {d['year']}")