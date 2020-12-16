"""
You are given an integer n representing the length of an n by n board. Remove all cells that are diagonal to one of the four corners (top left, top right, bottom right, and bottom left) and return the number of empty cells leftover
"""

import unittest


def method_name(n):
    return n*n - 2 * n + (n%2)



# Add these test cases, and remove this placeholder

# 1. Test Cases from the Examples of Problem Statement
# 2. Other Simple Cases
# 3. Corner/Edge Cases
# 4. Large Inputs

# DO NOT TOUCH THE BELOW CODE
class TestMethodName(unittest.TestCase):

    def test_01(self):
        input_nums = 4
        output_nums = 8

        self.assertEqual(method_name(input_nums), output_nums) 
    def test_02(self):
        input_nums = 4
        output_nums = 8

        self.assertEqual(method_name(input_nums), output_nums) 
    def test_03(self):
        input_nums = 4
        output_nums = 8

        self.assertEqual(method_name(input_nums), output_nums)  
    def test_04(self):
        input_nums = 4
        output_nums = 8

        self.assertEqual(method_name(input_nums), output_nums)  

if __name__ == '__main__':
    unittest.main(verbosity=2)
