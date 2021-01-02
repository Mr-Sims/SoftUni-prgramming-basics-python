sub = input()
text = input()
# print(text.replace(sub, ""))


while sub in text:
    text = text.replace(sub, "")

print(text)