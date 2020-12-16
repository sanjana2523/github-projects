"""
Given a list of integers nums, swap each consecutive even indexes with each other, and swap each consecutive odd indexes with each other.
"""

import unittest


def method_name(nums):
    length = len(nums)
    for i in range(0,length,4):
        if(i+2<length):
            nums[i], nums[i+2] = nums[i+2], nums[i]
        if(i+3<length):
            nums[i+1], nums[i+3] = nums[i+3], nums[i+1]
    return nums


# Add these test cases, and remove this placeholder

# 1. Test Cases from the Examples of Problem Statement
# 2. Other Simple Cases
# 3. Corner/Edge Cases
# 4. Large Inputs

# DO NOT TOUCH THE BELOW CODE
class TestMethodName(unittest.TestCase):

   def test_01(self):
        input_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        output_nums = [2, 3, 0, 1, 6, 7, 4, 5, 8]

        self.assertEqual(method_name(input_nums), output_nums)

   def test_02(self):
        input_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        output_nums = [2, 3, 0, 1, 6, 7, 4, 5, 8]

        self.assertEqual(method_name(input_nums), output_nums)

   def test_03(self):
        input_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        output_nums = [2, 3, 0, 1, 6, 7, 4, 5, 8]

        self.assertEqual(method_name(input_nums), output_nums)       

   def test_04(self):
        input_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        output_nums = [2, 3, 0, 1, 6, 7, 4, 5, 8]

        self.assertEqual(method_name(input_nums), output_nums)     


if __name__ == '__main__':
    unittest.main(verbosity=2)
