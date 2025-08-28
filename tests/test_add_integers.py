import unittest
from solutions.add_integers import Solution

class Solution:
    def add(self, a: int, b: int) -> int:
        return a + b

class TestAddIntegers(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_add(self):
        self.assertEqual(self.solution.add(1, 2), 3)
        self.assertEqual(self.solution.add(-1, 1), 0)
        self.assertEqual(self.solution.add(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()
