numbers = {1: "one", 2 : "two", 3 : "three"}

for key, value in numbers.items():
    print(value)

my_dict = {'Peter': 21, 'George': 18, 'John': 45}

sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse= False))

print(sorted_dict)