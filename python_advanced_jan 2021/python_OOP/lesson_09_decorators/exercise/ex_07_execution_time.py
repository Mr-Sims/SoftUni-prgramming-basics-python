import functools
import time


def exec_time(func):
    @functools.wraps(func)
    def wrapper(*args):
        start = time.time()
        func(*args)
        end = time.time()
        return end - start

    return wrapper



## Test case 1
@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total
print(loop(1, 10000000))


# Test case 2
@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result
print(concatenate(["a" for i in range(1000000)]))




# # test first zero
# import unittest
# import time
#
# class ExecTimeTests(unittest.TestCase):
#     def test_zero_first(self):
#         @exec_time
#         def loop(start, end):
#             total = 0
#             for x in range(start, end):
#                 total += x
#             return total
#         self.assertEqual(round(loop(1, 10000000)), 1)
#
# if __name__ == '__main__':
#     unittest.main()
#

# # test second zero
# import unittest
# import time
#
# class ExecTimeTests(unittest.TestCase):
#     def test_zero_second(self):
#         @exec_time
#         def concatenate(strings):
#             result = ""
#             for string in strings:
#                 result += string
#             return result
#         self.assertEqual(round(concatenate(["a" for i in range(1000000)])), 0)
#
# if __name__ == '__main__':
#     unittest.main()