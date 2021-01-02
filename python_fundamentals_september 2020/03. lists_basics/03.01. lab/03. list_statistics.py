n = int(input())
positive = []
negative = []
sum_neg = 0
for el in range(0, n):
    integer = int(input())
    if integer >= 0:
        positive.append(integer)
    else:
        negative.append(integer)

# for integer in range(len(negative)):
#     sum_neg += negative[integer]

print(positive)
print(negative)
#print(f"Count of positives: {len(positive)}. Sum of negatives: {sum_neg}")
print(f"Count of positives: {len(positive)}. Sum of negatives: {sum(negative)}")


