"""
Given strings older and newer, each representing software package versions in the format major.minor.patch, return whether the newer version is actually newer than the older.
"""

import unittest


def method_name(older,newer):
    older = older.split('.')
    newer=newer.split('.')
    for o, n in zip(older, newer):
        if int(n)>int(o):
            return True
        elif int(n)<int(o):
            return False
    return False


# Add these test cases, and remove this placeholder

# 1. Test Cases from the Examples of Problem Statement
# 2. Other Simple Cases
# 3. Corner/Edge Cases
# 4. Large Inputs

# DO NOT TOUCH THE BELOW CODE
class TestMethodName(unittest.TestCase):

    def test_01(self):
        older = "11.1.2"
        newer = "11.1.3"
        output_nums = True

        self.assertEqual(method_name(older,newer), output_nums)

    def test_02(self):
        older = "3.1.2"
        newer = "1.1.3"
        output_nums = False

        self.assertEqual(method_name(older,newer), output_nums)

    def test_03(self):
        older = "3.1.2"
        newer = "3.2.3"
        output_nums = True

        self.assertEqual(method_name(older,newer), output_nums)    

    def test_04(self):
        older = "13.1.2"
        newer = "3.2.3"
        output_nums = False

        self.assertEqual(method_name(older,newer), output_nums)    

if __name__ == '__main__':
    unittest.main(verbosity=2)
