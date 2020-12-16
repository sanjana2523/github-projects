# N-rooks [binarysearch.io satus:solved ,Level:easy]
"""
??? You've got an integer n representing a chessboard of size n x n. Return the number of ways you can place n rooks, such that no two rooks attack each other.

Two ways are considered different if in one of the ways, some cell of the chessboard is occupied, and in the other way, the cell is not occupied.

Note: two rooks are attacking each other if they are either on the same row or on the same column.

Example 1
Input

n = 3
Output

6
Explanation

Here are the different chessboard configurations, where X is a rook.

X O O
O X O
O O X

X O O
O O X
O X O

O X O
X O O
O O X

O X O
O O X
X O O

O O X
O X O
X O O

O O X
X O O
O X O

 ???
"""

import unittest


def n_rooks(n):
    """
    ??? Write what needs to be done ???
    """
    a = 0
    b = 1
    if n == 1 or n == 0:
        return b
    else:
        for i in range(2, n+1):
            c = b*i
            a = b
            b = c
        return b

# Add these test cases, and remove this placeholder

# 1. Test Cases from the Examples of Problem Statement
# 2. Other Simple Cases
# 3. Corner/Edge Cases
# 4. Large Inputs

# DO NOT TOUCH THE BELOW CODE


class TestNrooks(unittest.TestCase):

    def test_01(self):
        input_nums = 3
        output_nums = 6

        self.assertEqual(n_rooks(input_nums), output_nums)

    def test_02(self):
        input_nums = 6
        output_nums = 720

        self.assertEqual(n_rooks(input_nums), output_nums)

    def test_03(self):
        input_nums = 2
        output_nums = 2

        self.assertEqual(n_rooks(input_nums), output_nums)

    def test_04(self):
        input_nums = 15
        output_nums = 1307674368000

        self.assertEqual(n_rooks(input_nums), output_nums)


if __name__ == '__main__':
    unittest.main(verbosity=2)
