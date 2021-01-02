#############################################################################################
############################ Решение 60/100 #################################################
#############################################################################################

sequence = [int(el) for el in input().split()]
skip = int(input()) - 1
victim = skip
dead = []
while True:
    dead.append(sequence.pop(victim))
    if len(sequence) == 0:
        break
    victim = (victim + skip) % len(sequence)
dead = ",".join([str(i) for i in dead])
print(f"[{dead}]")

##################################################################################################
#################################  Чуждо решение  ################################################################


# numbers = input().split(" ")
# jump = int(input())
# iter = jump - 1
# result = ""
#
# while True:
#     if len(numbers) == 0:
#         break
#
#     while iter >= len(numbers):
#         iter = iter - len(numbers)
#
#     result += f"{numbers[iter]},"
#     numbers.pop(iter)
#
#     iter += jump - 1
#
# result = result[:-1]
# print(f"[{result}]")



