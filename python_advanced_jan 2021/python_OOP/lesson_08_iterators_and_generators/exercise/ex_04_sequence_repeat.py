class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = 0
        self.seq = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.number:
            raise StopIteration
        res = self.sequence[self.seq]
        self.index += 1
        self.seq += 1
        if self.seq == len(self.sequence):
            self.seq = 0
        return res



result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')