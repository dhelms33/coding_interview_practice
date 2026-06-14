import unittest
from Palindrome import is_palindrome_str

class Testing:
    def __init__(self):
        pass
    
    def palindrome_test(self):
        self.assertAlmostEqual(is_palindrome_str("DD"), True)
        self.assertRaises(TypeError, is_palindrome_str(55))