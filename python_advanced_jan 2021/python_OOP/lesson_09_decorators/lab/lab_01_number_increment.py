def number_increment(numbers):

    def increase():
        # nums = []
        # for num in numbers:
        #     nums.append(num+1)
        # return nums

        return [x + 1 for x in numbers]
    return increase()



print(number_increment([1, 2, 3]))