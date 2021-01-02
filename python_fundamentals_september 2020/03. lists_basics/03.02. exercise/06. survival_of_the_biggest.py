num_str = input()
nums_to_remove = int(input())

num_list = num_str.split()
for index in range(len(num_list)):
    num_list[index] = int(num_list[index])
for el in range(nums_to_remove):
    num_list.remove(min(num_list))

print(num_list)