import unittest
from solutions.can_construct import Solution

class TestCanConstruct(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        ransomNote = "a"
        magazine = "b"
        self.assertFalse(self.s.canConstruct(ransomNote, magazine))

    def test_example2(self):
        ransomNote = "aa"
        magazine = "ab"
        self.assertFalse(self.s.canConstruct(ransomNote, magazine))

    def test_example3(self):
        ransomNote = "aa"
        magazine = "aab"
        self.assertTrue(self.s.canConstruct(ransomNote, magazine))

    def test_empty_ransom(self):
        ransomNote = ""
        magazine = "abc"
        self.assertTrue(self.s.canConstruct(ransomNote, magazine))  # empty ransom is always possible

    def test_same_string(self):
        ransomNote = "hello"
        magazine = "hello"
        self.assertTrue(self.s.canConstruct(ransomNote, magazine))

if __name__ == "__main__":
    unittest.main()
