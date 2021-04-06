class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


import unittest


class IntegerListTests(unittest.TestCase):
    def test_integer_list_add__when_int_expect_to_add_it(self):#1
        integer_list = IntegerList()
        internal_list = integer_list.add(1)
        self.assertEqual([1], internal_list)

    def test_integer_list_add__when_str__expect_exception(self): #2
        integer_list = IntegerList()
        with self.assertRaises(ValueError):
            integer_list.add("as")

    def test_integer_list_remove_index_when_valid_index__expect_to_remove_and_return_it(self): #3
        value_to_be_removed = 3
        integer_list = IntegerList(1, 2, value_to_be_removed, 4)

        result = integer_list.remove_index(2)
        self.assertEqual(value_to_be_removed, result)
        self.assertEqual([1, 2, 4], integer_list.get_data())

    def test_integer_list_remove_index__when_invalid_negative_index_expect_exception(self): #4
        integer_list = IntegerList(1, 2, 3)
        index = -4
        with self.assertRaises(IndexError):
            integer_list.remove_index(index)

    def test_integer_list_remove_index__when_invalid_positive_index_expect_exception(self): #5
        integer_list = IntegerList(1, 2, 3)
        index = 3
        with self.assertRaises(IndexError):
            integer_list.remove_index(index)

    def test_integer_list_init__when_integers__expect_to_create_it(self): #6
        IntegerList(1, 2, 3)

    def test_integer_list_init__when_not_only_integers__expect_exception(self): #7
        with self.assertRaises(Exception):
            IntegerList(1, 2, "as")

    def test_integer_list_get__when_valid_index__except_to_return_it(self): #8
        value_to_be_returned = 3
        integer_list = IntegerList(1, 2, value_to_be_returned)
        result = integer_list.get(2)
        self.assertEqual(value_to_be_returned, result)

    def test_integer_list_get__when_invalid_negative_index_expect_exception(self): #9
        integer_list = IntegerList(1, 2, 3)
        index = -4
        with self.assertRaises(IndexError):
            integer_list.get(index)

    def test_integer_list_get__when_invalid_positive_index_expect_exception(self): #10
        integer_list = IntegerList(1, 2, 3)
        index = 3
        with self.assertRaises(IndexError):
            integer_list.get(index)

    def test_integer_list_insert__when_valid_index_and_value__except_to_insert_it(self): #11
        integer_list = IntegerList(1, 2, 3)
        value_to_be_inserted = 4
        index_to_insert = 0
        integer_list.insert(index_to_insert, value_to_be_inserted)
        expected = [4, 1, 2, 3]
        result = integer_list.get_data()
        self.assertEqual(expected, result)

    # def test_integer_list_insert__when_invalid_negative_index_expect_exception(self): #12
    #     integer_list = IntegerList(1, 2, 3)
    #     value_to_be_inserted = 1
    #     index_to_insert = 3
    #
    #     with self.assertRaises(IndexError):
    #         integer_list.insert(index_to_insert, value_to_be_inserted)

    def test_integer_list_insert__when_invalid_positive_index_expect_exception(self): # 13
        integer_list = IntegerList(1, 2, 3)
        index_to_insert = 3
        value_to_insert = 1
        with self.assertRaises(IndexError):
            integer_list.insert(index_to_insert, value_to_insert)

    def test_integer_list_insert__when_value_is_str_expect_exception(self): #14
        integer_list = IntegerList(1, 2, 3)
        index_to_insert = 1
        value_to_insert = "asd"
        with self.assertRaises(ValueError):
            integer_list.insert(index_to_insert, value_to_insert)

    def test_integer_get_biggest__expect_to_return_the_biggest(self): #15
        biggest = 17
        integer_list = IntegerList(1, 2, biggest, 3, 4)
        actual = integer_list.get_biggest()
        self.assertEqual(biggest, actual)

    def test_integer_list_get_index__when_value_in_list__expect_to_return_the_index(self): #16
        integer_list = IntegerList(1, 2, 3, 4)
        index = 2
        el = 3
        res = integer_list.get_index(el)
        self.assertEqual(index, res)

    # def test_integer_list_get_index__when_value_not_in_list__expect_exception(self): # 17
    #     integer_list = IntegerList(1, 2, 3)
    #     value = 2
    #     el = 6
    #     with self.assertRaises(IndexError):
    #         integer_list.get_index(el)


if __name__ == '__main__':
    unittest.main()


# Constraints
# add operation, should add an element and returns the list.  #1
# If the element is not an integer, a ValueError is thrown #2
# remove_index operation removes the element on that index and returns it. #3
# If the index is out of range, an IndexError is thrown #4 pos, #5 neg
# __init__ should only take integers, and store them #6, #7
# get should return the specific element #8
# If the index is out of range, an IndexError is thrown #9 neg, #10 pos
# insert #11 when valid
# If the index is out of range, IndexError is thrown #12 neg, #13 pos
# If the element is not an integer, ValueError is thrown # 14 str
# get_biggest #15
# get_index #16 when_in_list, #17 when_not_in_list
