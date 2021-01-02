num = list(input())


def odd_even_sum(lst):
    even = 0
    odd = 0
    for el in num:
        if int(el) % 2 == 0:
            even += int(el)
        else:
            odd += int(el)
    res = f"Odd sum = {odd}, Even sum = {even}"
    return res


print(odd_even_sum(num))





