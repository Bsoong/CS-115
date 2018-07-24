'''
Created on Oct 3, 2017

@author: brand
I pledge my honor that I have abided by the Stevens Honor System - Bsoong
'''

import unittest
import hw4

class Test(unittest.TestCase):
    """10 tests, 5 for pascal_row, 5 for pascal_triangle"""
    def test0(self):
        self.assertEqual(hw4.pascal_row(0), [1])
    def test1(self):
        self.assertEqual(hw4.pascal_row(1), [1,1])
    def test2(self):
        self.assertEqual(hw4.pascal_row(2), [1,2,1])
    def test3(self):
        self.assertEqual(hw4.pascal_row(3), [1,3,3,1])
    def test4(self):
        self.assertEqual(hw4.pascal_row(4), [1,4,6,4,1])
        
        
    def test5(self):
        self.assertEqual(hw4.pascal_triangle(0), [[1]])
    def test6(self):
        self.assertEqual(hw4.pascal_triangle(1), [[1],[1,1]])
    def test7(self):
        self.assertEqual(hw4.pascal_triangle(2), [[1], [1, 1], [1, 2, 1]])
    def test8(self):
        self.assertEqual(hw4.pascal_triangle(3), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])
    def test9(self):
        self.assertEqual(hw4.pascal_triangle(4), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])

if __name__ == "__main__":
    unittest.main()       