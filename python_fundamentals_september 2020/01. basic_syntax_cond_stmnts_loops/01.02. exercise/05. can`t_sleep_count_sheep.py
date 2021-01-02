# If you can't sleep, just count sheep!
# Given a non-negative integer, 3 for example, return a string with a murmur:
# "1 sheep...2 sheep...3 sheep..." Input will always be valid, i.e. no negative integers.

# sheep = int(input())
#
# for i in range(1, sheep + 1):
#     print(f"{i} sheep...", end='')

sheep_count = int(input())
message = ''
sheep = 0

while sheep < sheep_count:
    message += f'{sheep + 1} sheep...'
    sheep += 1
print(message)