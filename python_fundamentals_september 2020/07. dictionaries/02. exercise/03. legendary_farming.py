#######################################################################
####################### Мое решение 40/100 #################################33
# key_materials = {"fragments": 0, 'shards' : 0, 'motes': 0}
# junk_materials = {}
# legendary = False
#
# while not legendary:
#     line = input().split()
#     for el in range(1, len(line), 2):
#         word_lower = line[el].lower()
#
#         if word_lower not in key_materials:
#             junk_materials[word_lower] = int(line[el-1])
#         else:
#             key_materials[word_lower] += int(line[el-1])
#
#         if  key_materials.get("fragments") >= 250:
#             print('Valanyr obtained!')
#             key_materials['fragments'] -= 250
#             legendary = True
#             break
#         elif key_materials.get("shards") >= 250:
#             print('Shadowmourne obtained')
#             key_materials['shards'] -= 250
#             legendary = True
#             break
#         elif key_materials.get("motes") >= 250:
#             print('Dragonwrath obtained!')
#             key_materials['motes'] -= 250
#             legendary = True
#             break
#
#
# sorted_key = sorted(key_materials.items(), key=lambda x: (-x[1], x[0]))
# for key, value in sorted_key:
#     print(f"{key}: {value}")
#
# sorted_junk = dict(sorted(junk_materials.items(), key=lambda x: x[0]))
# for key, value in sorted_junk.items():
#     print(f"{key}: {value}")


#######################################################################
####################### решение Инес #################################

mapper = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}

key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk_materials = {}

while True:
    line = input().split()
    legendary = False
    for i in range(0, len(line), 2):
        qnty = int(line[i])
        item = line[i+1].lower()

        if item in key_materials:
            key_materials[item] += qnty
        else:
            if item not in junk_materials:
                junk_materials[item] = qnty
            else:
                junk_materials[item] += qnty

        for key, value in key_materials.items():
            if value >= 250:
                print(f"{mapper[key]} obtained!")
                key_materials[key] -= 250
                legendary = True
                break
        if legendary:
            break
    if legendary:
        break
sorted_key = sorted(key_materials.items(), key=lambda x: (-x[1], x[0]))
for key, value in sorted_key:
    print(f"{key}: {value}")

sorted_junk = dict(sorted(junk_materials.items(), key=lambda x: x[0]))
for key, value in sorted_junk.items():
    print(f"{key}: {value}")









