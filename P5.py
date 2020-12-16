"""
Given a list of integers nums, squeeze from both the left and the right of nums until there is one remaining element. Return the states at each step.
"""

import unittest


def method_name(nums):
    ret = [nums] 
    while len(nums) > 1: 
        if len(nums) == 2: 
            nums = [nums[0] + nums[1]] 
        elif len(nums) == 3: 
            nums = [nums[0] + nums[1] + nums[2]] 
        else: 
            nums = [nums[0] + nums[1]] + nums[2:-2] + [nums[-2] + nums[-1]] 
        ret.append(nums) 
    return ret    


# Add these test cases, and remove this placeholder

# 1. Test Cases from the Examples of Problem Statement
# 2. Other Simple Cases
# 3. Corner/Edge Cases
# 4. Large Inputs

# DO NOT TOUCH THE BELOW CODE
class TestMethodName(unittest.TestCase):

 def test_01(self):
        input_nums = [1, 2, 3, 4, 5, 6]
        output_nums =[
                    [1, 2, 3, 4, 5, 6],
                    [3, 3, 4, 11],
                    [6, 15],
                    [21]
                     ]

        self.assertEqual(method_name(input_nums), output_nums)

 def test_02(self):
        input_nums = [1, 2, 3, 4, 5]
        output_nums =[
                    [1, 2, 3, 4, 5],
                    [3, 3, 9],
                    [15],
                     ]

        self.assertEqual(method_name(input_nums), output_nums)

 def test_03(self):
        input_nums = [1, 2, 3, 4, 5, 6]
        output_nums =[
                    [1, 2, 3, 4, 5, 6],
                    [3, 3, 4, 11],
                    [6, 15],
                    [21]
                     ]

        self.assertEqual(method_name(input_nums), output_nums)

 def test_04(self):
        input_nums = [1, 2, 3, 4, 5]
        output_nums =[
                    [1, 2, 3, 4, 5],
                    [3, 3, 9],
                    [15],
                     ]

        self.assertEqual(method_name(input_nums), output_nums)       

      
if __name__ == '__main__':
    unittest.main(verbosity=2)
