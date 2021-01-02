######################### НАЙ-ДОБРО РЕШЕНИЕ ###################################


def perfect(a):
    divisor = [int(el) for el in range(1, a) if a % el == 0]
    if sum(divisor) == a:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


num = int(input())
print(perfect(num))

######################## ПЪРВОТО РАБОТЕЩО РЕШЕНИЕ ###################################

# num = int(input())
#
#
# def perfect(a):
#     divisor = []
#     for i in range(1, a):
#         if a % i == 0:
#             divisor.append(i)
#     res = sum(divisor)
#     if res == a:
#         return "We have a perfect number!"
#     else:
#         return "It's not so perfect."
#
#
# print(perfect(num))

###################### МОЕ РЕШЕНИЕ Първоначално ###############################




# num = int(input())
# divisors_list = []
#
# def perfect_num(a):
#     perfect = False
#     for div_1 in range(1, a+1):
#         for div_2 in range(1, a+1):
#             if div_1 * div_2 == a:
#                 divisors_list.append(int(div_2))
#                 divisors_list.append(int(div_1))
#     divisors_set = set(divisors_list)
#     new_list = list(divisors_set)
#     del new_list[-1]
#     if sum(new_list) == num:
#         perfect = True
#         return "We have a perfect number!"
#     else:
#         return "It's not so perfect."
#
#
# print(perfect_num(num))

####################################  МОЕ РЕШЕНИЕ 2 - CHEAT  ###########################################

# num = int(input())
#
#
# def perfect_num(a):
#     perfect_number_list = [6, 28, 496, 8128, 33550336, 8589869056, 137438691328, 2305843008139952128, 2658455991569831744654692615953842176]
#     if a in perfect_number_list:
#         return "We have a perfect number!"
#     else:
#         return "It's not so perfect."
#
#
# print(perfect_num(num))

##############################################################################################################




############################ ЧУЖДО РЕШЕНИЕ ##################
def perfect_number(n):
    iterator = n
    sum = 0
    while True:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n // 2 + 1
        sum += n
        if n <= 1:
            break
    if sum == iterator:
        output_flag = True
    else:
        output_flag = False

    return output_flag


a = int(input())
result = perfect_number(a)
if result == True:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")

############################# ЧУЖДО РЕШЕНИЕ 2 ##################################

number = int(input())


def perfect_number():
    count = 0
    for current_num in range(1, number):
        while number % current_num == 0:
            count += current_num
            break
    if count == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")
