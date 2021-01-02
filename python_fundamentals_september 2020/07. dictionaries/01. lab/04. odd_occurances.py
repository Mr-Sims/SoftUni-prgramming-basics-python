line = input().split()

my_dict = {}

for word in line:
    word_low = word.lower()
    if word_low not in my_dict:
        my_dict[word_low] = 0
    my_dict[word_low] += 1

for key, value in my_dict.items():
    if value % 2 != 0:
        print(key, end=" ")