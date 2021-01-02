###################################################################################################################
#####################################  Nested dict ###########################################################

peter_dict = {}
line = input()

while line != "Log out":
    data = line.split(": ")
    command = data[0]

    if command == "New follower":
        new_follower = data[1]
        if new_follower in peter_dict:
            pass
        elif new_follower not in peter_dict:
            peter_dict[new_follower] = {"likes": 0, "comments": 0}

    elif command == "Like":
        follower = data[1]
        likes = int(data[2])
        if follower in peter_dict:
            if peter_dict[follower]["likes"] == 0:
                peter_dict[follower]["likes"] = likes
            else:
                peter_dict[follower]["likes"] += likes
        else:
            peter_dict[follower] = {"likes": likes, "comments": 0}

    elif command == "Comment":
        follower = data[1]
        if follower in peter_dict:
            peter_dict[follower]["comments"] += 1
        else:
            peter_dict[follower] = {"likes": 0, "comments": 1}
    elif command == "Blocked":
        follower = data[1]
        if follower in peter_dict:
            block = peter_dict.pop(follower)
        else:
            print(f"{follower} doesn't exist.")

    line = input()

print(f"{len(peter_dict)} followers")

filtered_followers = sorted(peter_dict.items(), key=lambda x: (x[1], -x[0]))

for key, value in filtered_followers:
    print(f"{key}: {value['likes']+value['comments']}")

###################################################################################################################
#####################################  dict + list ###########################################################


peter_dict = {}
line = input()

while line != "Log out":
    data = line.split(": ")
    command = data[0]

    if command == "New follower":
        new_follower = data[1]
        if new_follower in peter_dict:
            pass
        elif new_follower not in peter_dict:
            peter_dict[new_follower] = [0, 0]

    elif command == "Like":
        follower = data[1]
        likes = int(data[2])
        if follower in peter_dict:
            peter_dict[follower][0] += likes
        else:
            peter_dict[follower] = [likes, 0]

    elif command == "Comment":
        follower = data[1]
        if follower in peter_dict:
            peter_dict[follower][1] += 1
        else:
            peter_dict[follower] = [0, 1]
    elif command == "Blocked":
        follower = data[1]
        if follower in peter_dict:
            block = peter_dict.pop(follower)
        else:
            print(f"{follower} doesn't exist.")

    line = input()
print(f"{len(peter_dict)} followers")
filter_dict = {}
for key,value in peter_dict.items():
    filter_dict[key] = sum(value)
filter_dict = dict(sorted(filter_dict.items(), key=lambda x:(-x[1],x[0])))
for key,value in filter_dict.items():
    print(f"{key}: {value}")





