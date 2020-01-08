import unittest
import sys
sys.path.append('../')
from normalize import normalize

class NormalizeTestMethods(unittest.TestCase):
    
    def test_empty(self):
        actual = normalize([])
        self.assertEqual(actual, [])

    def test_one(self):
        actual = normalize([1])
        self.assertEqual(actual, [1])

    def test_zero(self):
        actual = normalize([0])
        self.assertEqual(actual, [])

    def test_divide_by_first(self):
        actual = normalize([2,5,8])
        self.assertEqual(actual, [1, 2.5, 4])

if __name__ == '__main__':
    unittest.main()