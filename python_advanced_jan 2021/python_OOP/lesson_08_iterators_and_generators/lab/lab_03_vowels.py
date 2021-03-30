class vowels:
    vs = ["A", "E", "O", "U", "I", "a", "e", "o", "u", "i", "Y", "y"]

    def __init__(self, iterable):
        self.iterable = list(iterable)
        self.end = len(self.iterable)-1
        self.value = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        self.value += 1
        if self.iterable[self.value] not in vowels.vs:
            return self.__next__()
        return self.iterable[self.value]



my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)