"""
??? Question with two examples ???
"""

import unittest


def method_name(nums):
    """
    ??? Write what needs to be done ???
    """
    pass


# Add these test cases, and remove this placeholder

# 1. Test Cases from the Examples of Problem Statement
# 2. Other Simple Cases
# 3. Corner/Edge Cases
# 4. Large Inputs

# DO NOT TOUCH THE BELOW CODE
class TestMethodName(unittest.TestCase):

    def test_01(self):
        input_nums = [1, 2, 3, 4]
        output_nums = 10

        self.assertEqual(method_name(input_nums), output_nums)


if __name__ == '__main__':
    unittest.main(verbosity=2)
