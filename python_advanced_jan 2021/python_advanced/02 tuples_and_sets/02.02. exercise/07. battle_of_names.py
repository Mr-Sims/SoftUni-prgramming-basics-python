n = int(input())
even_set = set()
odd_set = set()
for i in range(1, n+1):
    line = input()
    letters_count = sum(ord(el) for el in line)
    current_sum = letters_count // i
    if current_sum % 2 == 0:
        even_set.add(current_sum)
    else:
        odd_set.add(current_sum)

sum_evens = sum(even_set)
sum_odds = sum(odd_set)

if sum_evens == sum_odds:
    modified_set = [str(el) for el in even_set.union(odd_set)]
    print(f"{', '.join(modified_set)}")
elif sum_odds > sum_evens:
    modified_set = [str(el) for el in odd_set.difference(even_set)]
    print(f"{', '.join(modified_set)}")
else:
    modified_set = [str(el) for el in odd_set.symmetric_difference(even_set)]
    print(f"{', '.join(modified_set)}")