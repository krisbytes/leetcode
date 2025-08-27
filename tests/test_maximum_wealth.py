import unittest
from solutions.maximum_wealth import Solution

class TestMaximumWealth(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        accounts = [[1,2,3],[3,2,1]]
        self.assertEqual(self.s.maximumWealth(accounts), 6)

    def test_example2(self):
        accounts = [[1,5],[7,3],[3,5]]
        self.assertEqual(self.s.maximumWealth(accounts), 10)

    def test_example3(self):
        accounts = [[2,8,7],[7,1,3],[1,9,5]]
        self.assertEqual(self.s.maximumWealth(accounts), 17)

    def test_single_customer(self):
        accounts = [[100,200,300]]
        self.assertEqual(self.s.maximumWealth(accounts), 600)

    def test_empty_accounts(self):
        accounts = [[]]
        self.assertEqual(self.s.maximumWealth(accounts), 0)

if __name__ == "__main__":
    unittest.main()
