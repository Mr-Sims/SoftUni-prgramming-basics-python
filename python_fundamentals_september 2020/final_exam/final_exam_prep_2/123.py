def move(message, n):
    letters_to_move = message[:n]
    second_part = message[n:]
    result = second_part + letters_to_move
    return result


def insert_value(message, i, val):
    first_part = message[:i]
    second_part = message[i:]
    result = first_part + val + second_part
    return result


encrypted_message = input()

data = input()

while not data == "Decode":
    spitted_data = data.split("|")
    command = spitted_data[0]
    if command == "Move":
        n_letters = int(spitted_data[1])
        encrypted_message = move(encrypted_message, n_letters)
    elif command == "Insert":
        index = int(spitted_data[1])
        value = spitted_data[2]
        encrypted_message = insert_value(encrypted_message, index, value)
    elif command == "ChangeAll":
        sub_str = spitted_data[1]
        val = spitted_data[2]
        encrypted_message = encrypted_message.replace(sub_str, val)
    data = input()

print(f"The decrypted message is: {encrypted_message}")

########################################################################################################################
############################################################################################################################

import re


pattern = r"(#|\|)(?P<item>[a-zA-Z\s]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>([0-9][0-9]{0,3}|10000))\1"

data = input()

matches = re.finditer(pattern, data)
items = []
total_calories = 0


for match in matches:
    result = match.groupdict()
    total_calories += int(result['calories'])
    items.append(result)

days = total_calories // 2000

print(f"You have food to last you for: {days} days!")

for item in items:
    print(f"Item: {item['item']}, Best before: {item['date']}, Nutrition: {item['calories']}")


########################################################################################################################
############################################################################################################################

n = int(input())
pieces = {}

for _ in range(n):
    data = input().split('|')
    pieces[data[0]] = {'composer': data[1], 'key': data[2]}

data = input()

while not data == "Stop":
    splitted_data = data.split('|')
    commmand = splitted_data[0]
    if commmand == "Add":
        piece, composer, key = splitted_data[1:]
        if piece in pieces:
            print(f"{piece} is already in the collection!")
        else:
            pieces[piece] = {'composer': composer, 'key': key}
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif commmand == "Remove":
        piece = splitted_data[1]
        if piece in pieces:
            del pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif commmand == "ChangeKey":
        piece, new_key = splitted_data[1:]
        if piece in pieces:
            pieces[piece]['key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    data = input()

sorted_pieces = sorted(pieces.items(), key=lambda x: (x[0], x[1]['composer']))



########################################################################################################################
############################################################################################################################


n = int(input())
plants = {}


for _ in range(n):
    plant, rarity = input().split('<->')
    plants[plant] = {'rarity': int(rarity), 'ratings': []}

data = input()

while not data == "Exhibition":
    command, value = data.split(': ')
    try:
        if command == "Rate":
            plant, rating = value.split(" - ")
            plants[plant]['ratings'].append(int(rating))
        elif command == "Update":
            plant, rarity = value.split(" - ")
            plants[plant]['rarity'] = int(rarity)
        elif command == "Reset":
            plant = value
            plants[plant]['ratings'].clear()
    except:
        print("error")
    data = input()

for plant_name, plants_data in plants.items():
    if plants[plant_name]['ratings']:
        plants[plant_name]['avg'] = sum(plants[plant_name]['ratings'])/len(plants[plant_name]['ratings'])
    else:
        plants[plant_name]['avg'] = 0

sorted_plants = sorted(plants.items(), key=lambda x: (x[1]['rarity'], x[1]['avg']), reverse=True)

print("Plants for the exhibition:")
for plant_name, value in sorted_plants:
    print(f"- {plant_name}; Rarity: {value['rarity']}; Rating: {value['avg']:.2f}")


########################################################################################################################
############################################################################################################################

regex za emoji decorator -
(::|\*\*)(?P<emoji>[A-Z][a-z]{2,})\

import re

text = input()

pattern = r"(:{2}|\*{2})(?P<emoji>[A-Z]{1}[a-z]{2,})\1"

cool_threshold = 1
numbers = re.findall(r"\d", text)

for n in range(len(numbers)):
    cool_threshold *= int(numbers[n])

emojis_dict = {}
emojis = re.finditer(pattern, text)
for emoji in emojis:
    emoji_value = 0
    e = emoji.group()
    for char in e:
        if char.isalpha():
            emoji_value += ord(char)
    emojis_dict[e] = emoji_value

print(f"Cool threshold: {cool_threshold}")
print(f"{len(emojis_dict)} emojis found in the text. The cool ones are:")
for el in emojis_dict:
    if emojis_dict[el] >= cool_threshold:
        print(el)



########################################################################################################################
##########################################################################################################################

n = int(input())
plants = {}


for _ in range(n):
    plant, rarity = input().split('<->')
    plants[plant] = {'rarity': int(rarity), 'ratings': []}

data = input()

while not data == "Exhibition":
    command, value = data.split(': ')
    try:
        if command == "Rate":
            plant, rating = value.split(" - ")
            plants[plant]['ratings'].append(int(rating))
        elif command == "Update":
            plant, rarity = value.split(" - ")
            plants[plant]['rarity'] = int(rarity)
        elif command == "Reset":
            plant = value
            plants[plant]['ratings'].clear()
    except:
        print("error")
    data = input()

for plant_name, plants_data in plants.items():
    if plants[plant_name]['ratings']:
        plants[plant_name]['avg'] = sum(plants[plant_name]['ratings'])/len(plants[plant_name]['ratings'])
    else:
        plants[plant_name]['avg'] = 0

sorted_plants = sorted(plants.items(), key=lambda x: (x[1]['rarity'], x[1]['avg']), reverse=True)

print("Plants for the exhibition:")
for plant_name, value in sorted_plants:
    print(f"- {plant_name}; Rarity: {value['rarity']}; Rating: {value['avg']:.2f}")


# ##########################################################################################################################
############################################################################################################################
# ########################################################################################################################
############################################################################################################################
# ########################################################################################################################
#############################################################################################################################
# #######################################################################################################################
##########################################################################################################################
# ##########################################################################################################################
############################################################################################################################