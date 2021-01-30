def winner(neg, pos):
    if abs(sum(neg)) > sum(pos):
        return f"The negatives are stronger than the positives"
    else:
        return f"The positives are stronger than the negatives"


line = [int(x) for x in input().split()]

negative_nums = list(filter(lambda x: x < 0, line))
positive_nums = list(filter(lambda x: x >= 0, line))

print(sum(negative_nums))
print(sum(positive_nums))

print(winner(negative_nums, positive_nums))