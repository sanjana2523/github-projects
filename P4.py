"""
Given a list of strings book, page an index (0-indexed) into the book, and page_size, return the list of words on that page.

"""

import unittest

def method_name(book, page, page_size):
    l=page*page_size
    return book[l:l+page_size]


# Add these test cases, and remove this placeholder

# 1. Test Cases from the Examples of Problem Statement
# 2. Other Simple Cases
# 3. Corner/Edge Cases
# 4. Large Inputs

# DO NOT TOUCH THE BELOW CODE
class TestMethodName(unittest.TestCase):

   def test_01(self):
        book = ["concrete", "genuine", "plaster", "compact", "operation", "truth", "west"]
        page = 1
        page_size = 3
        output_nums = ["compact", "operation", "truth"]
        self.assertEqual(method_name(book, page, page_size), output_nums)

   def test_02(self):
        book = ["concrete", "genuine", "plaster", "compact", "operation", "truth", "west"]
        page = 1
        page_size = 3
        output_nums = ["compact", "operation", "truth"]
        self.assertEqual(method_name(book, page, page_size), output_nums)

   def test_03(self):
        book = ["concrete", "genuine", "plaster", "compact", "operation", "truth", "west"]
        page = 1
        page_size = 3
        output_nums = ["compact", "operation", "truth"]
        self.assertEqual(method_name(book, page, page_size), output_nums)

   def test_04(self):
        book = ["concrete", "genuine", "plaster", "compact", "operation", "truth", "west"]
        page = 1
        page_size = 3
        output_nums = ["compact", "operation", "truth"]
        self.assertEqual(method_name(book, page, page_size), output_nums)


if __name__ == '__main__':
    unittest.main(verbosity=2)
