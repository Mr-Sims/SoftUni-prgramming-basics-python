# Напишете програма, която да принтира на конзолата всички комбинации от 3 букви в зададен интервал,
# като се пропускат комбинациите съдържащи зададена от конзолата буква.
# Накрая трябва да се изпринтира броят на отпечатаните комбинации.
# Вход
# Входът се чете от конзолата и съдържа точно 3 реда:

# Ред 2.	Малка буква от английската азбука за край на интервала  – от първата буква до ‚z’.
# Ред 3.	Малка буква от английската азбука – от ‘a’ до ‚z’ – като комбинациите съдържащи тази буквата се пропускат.
# Изход
# Да се отпечатат на един ред всички комбинации отговарящи на условието плюс броят им разделени с интервал.
letter1 = input()#Малка буква от английската азбука за начало на интервала – от ‘a’ до ‚z’.
letter2 = input()#Малка буква от английската азбука за край на интервала  – от първата буква до ‚z’.
letter3 = input()#Малка буква от английската азбука – от ‘a’ до ‚z’ – като комбинациите съдържащи тази буквата се пропускат.
combo_counter = 0
for i in range(ord(letter1), ord(letter2)+1):

    for j in range(ord(letter1), ord(letter2)+1):

        for k in range(ord(letter1), ord(letter2)+1):
            if k != ord(letter3) and i != ord(letter3) and j != ord(letter3):
                print(f"{chr(i)}{chr(j)}{chr(k)}", end = " ")
                combo_counter += 1
print(combo_counter)