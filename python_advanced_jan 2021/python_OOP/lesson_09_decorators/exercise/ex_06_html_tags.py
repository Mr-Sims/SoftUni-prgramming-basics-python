import functools


def tags(tag):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):

            return f"<{tag}>{func(*args)}</{tag}>"
        return wrapper
    return decorator


# ## Test case 1
# @tags('p')
# def join_strings(*args):
#     return "".join(args)
# print(join_strings("Hello", " you!"))
#
# ## Test case 2
# @tags('h1')
# def to_upper(text):
#     return text.upper()
# print(to_upper('hello'))

# test first zero
import unittest

class TagsTests(unittest.TestCase):
    def test_zero_first(self):
        @tags('p')
        def join_strings(*args):
            return "".join(args)
        self.assertEqual(join_strings("Hello", " you!"), '<p>Hello you!</p>')

if __name__ == '__main__':
    unittest.main()