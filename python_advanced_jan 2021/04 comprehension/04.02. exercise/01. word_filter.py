def filtering():
    return [x for x in input().split(" ") if len(x) % 2 == 0]


def print_result(filtered):
    for i in filtered:
        print(i)


filtered = filtering()
print_result(filtered)

########################################################################################################
######################## oneliner

print(*[word for word in input().split() if len(word) % 2 == 0], sep='\n')
