country_dict = zip(input().split(", "), input().split(", "))
print(*[f"{x[0]} -> {x[1]}" for x in country_dict], sep="\n")

####################################################
### only list
countries = input().split(", ")
capitals = input().split(", ")
print(*[f'{countries[index]} -> {capitals[index]}' for index in range(len(capitals))], sep="\n")

###########################################################
### oneliner

print(*[f"{x[0]} -> {x[1]}" for x in zip(input().split(", "), input().split(", "))], sep="\n")