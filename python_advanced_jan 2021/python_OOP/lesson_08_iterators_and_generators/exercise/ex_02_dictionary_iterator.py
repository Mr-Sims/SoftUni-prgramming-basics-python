class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.dictionary)-1:
            raise StopIteration
        self.index += 1
        key = list(self.dictionary.keys())[self.index]
        return key, self.dictionary[key]



result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

# # test zero
# import unittest
#
#
# class DictionaryIteratorTests(unittest.TestCase):
#     def test_zero(self):
#         result = dictionary_iter({1: "1", 2: "2"})
#         expected = []
#         for x in result:
#             expected.append(x)
#         self.assertEqual(expected, [(1, "1"), (2, "2")])
#
#
# if __name__ == '__main__':
#     unittest.main()