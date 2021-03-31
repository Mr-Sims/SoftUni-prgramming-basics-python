class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.end = 0
        self.index = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == -1:
            raise StopIteration

        res = self.index
        self.index -= 1
        return res


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")