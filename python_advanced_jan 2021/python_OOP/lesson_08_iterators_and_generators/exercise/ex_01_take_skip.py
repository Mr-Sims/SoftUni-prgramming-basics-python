class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.index = 0
        self.end = self.step * self.count

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.end:
            raise StopIteration
        index = self.index
        self.index += self.step
        return index


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)