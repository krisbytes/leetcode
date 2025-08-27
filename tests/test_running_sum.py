import unittest
from solutions.running_sum import Solution

class TestRunningSum(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        # LeetCode sample input/output
        nums = [1,2,3,4]
        expected = [1,3,6,10]
        self.assertEqual(self.s.runningSum(nums), expected)

    def test_example2(self):
        nums = [1,1,1,1,1]
        expected = [1,2,3,4,5]
        self.assertEqual(self.s.runningSum(nums), expected)

    def test_example3(self):
        nums = [3,1,2,10,1]
        expected = [3,4,6,16,17]
        self.assertEqual(self.s.runningSum(nums), expected)

if __name__ == "__main__":
    unittest.main()
