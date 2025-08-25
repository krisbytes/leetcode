import unittest
from solutions.fizz_buzz import Solution

class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        self.assertEqual(
            self.s.fizzBuzz(3),
            ["1", "2", "Fizz"]
        )

    def test_example2(self):
        self.assertEqual(
            self.s.fizzBuzz(5),
            ["1", "2", "Fizz", "4", "Buzz"]
        )

    def test_example3(self):
        self.assertEqual(
            self.s.fizzBuzz(15)[-1],  # only check the last element
            "FizzBuzz"
        )

    def test_single_number(self):
        self.assertEqual(
            self.s.fizzBuzz(1),
            ["1"]
        )

    def test_large(self):
        result = self.s.fizzBuzz(20)
        self.assertEqual(result[2], "Fizz")   # 3rd element
        self.assertEqual(result[4], "Buzz")   # 5th element
        self.assertEqual(result[14], "FizzBuzz")  # 15th element

if __name__ == "__main__":
    unittest.main()
