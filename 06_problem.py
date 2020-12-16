"""
Given a list of lowercase alphabet strings words, return the length of the longest contiguous sublist where all words share the same first letter.
"""

import unittest


def method_name(words):
    maxlength = 0
    curr_letter, curr_length = None, 0
    for word in words:
         if not curr_letter or curr_letter != word[0]:
            maxlength = max(maxlength, curr_length)
            curr_letter, curr_length = word[0], 1
         else:
            curr_length += 1
    return max(maxlength, curr_length)


# Add these test cases, and remove this placeholder

# 1. Test Cases from the Examples of Problem Statement
# 2. Other Simple Cases
# 3. Corner/Edge Cases
# 4. Large Inputs

# DO NOT TOUCH THE BELOW CODE
class TestMethodName(unittest.TestCase):

    def test_01( self):
        words = ["she", "sells", "seashells", "he", "sells", "clams"]
        output_nums = 3

        self.assertEqual(method_name( words), output_nums)

    def test_02( self):
        words = ["she", "sells", "seashells", "he", "sells", "clams"]
        output_nums = 3

        self.assertEqual(method_name( words), output_nums)

    def test_03( self):
        words = ["she", "sells", "seashells", "he", "sells", "clams"]
        output_nums = 3

        self.assertEqual(method_name( words), output_nums)
    def test_04( self):
        words = ["she", "sells", "seashells", "he", "sells", "clams"]
        output_nums = 3

        self.assertEqual(method_name( words), output_nums)    

if __name__ == '__main__':
    unittest.main(verbosity=2)
