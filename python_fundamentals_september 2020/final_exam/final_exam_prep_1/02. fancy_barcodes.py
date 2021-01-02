
import re
pattern = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"
n = int(input())
for _ in range(n):
    barcode_line = input()
    if re.match(pattern, barcode_line):
        digits = re.findall(r"\d", barcode_line)
        if digits:
            print(f"Product group: {''.join(digits)}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")

####################################################################################################
#
import re
pattern = r"(?P<first_symbol>@#{1,})(?P<barcode>[A-Z][A-Za-z0-9]{4,}[A-Z])(?P<last_symbol>@#{1,})"
barcodes_count = int(input())

for _ in range(barcodes_count):
    barcode = input()
    digits = ""
    is_valid = re.match(pattern, barcode)
    if is_valid:
        valid_barcode = is_valid.groupdict()
        for ch in valid_barcode["barcode"]:
            if ch.isdigit():
                digits += ch
        if len(digits) == 0:
            print(f"Product group: 00")
        else:
            print(f"Product group: {digits}")
    else:
        print("Invalid barcode")

###############################################################################################


import re
count = int(input())
pattern = r"(?P<prefix>^@#)(#+)?([A-Z][A-Za-z0-9]{4,})[A-Z](?P=prefix)(#+)?"
validation = r"\d+"
result = {}
all_barcodes = []
for code in range(count):
    barcode = input()
    all_barcodes.append(barcode)
    valid = re.finditer(pattern, barcode)
    valid = [el.group() for el in valid]
    nums = re.findall(validation, barcode)
    result[''.join(valid)] = nums

for barcode in all_barcodes:
    if barcode in result:
        if len(result[barcode]) == 0:
            result[barcode] = ["0", "0"]
        print(f"Product group: {''.join(result[barcode])}")
    else:
        print("Invalid barcode")