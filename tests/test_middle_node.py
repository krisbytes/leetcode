import unittest
from solutions.middle_node import Solution
from utils.linked_list import build_linked_list, linked_list_to_list

class TestMiddleNode(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        head = build_linked_list([1,2,3,4,5])
        middle = self.s.middleNode(head)
        self.assertEqual(linked_list_to_list(middle), [3,4,5])

    def test_example2(self):
        head = build_linked_list([1,2,3,4,5,6])
        middle = self.s.middleNode(head)
        self.assertEqual(linked_list_to_list(middle), [4,5,6])

    def test_single_node(self):
        head = build_linked_list([1])
        middle = self.s.middleNode(head)
        self.assertEqual(linked_list_to_list(middle), [1])

    def test_two_nodes(self):
        head = build_linked_list([1,2])
        middle = self.s.middleNode(head)
        self.assertEqual(linked_list_to_list(middle), [2])

if __name__ == "__main__":
    unittest.main()
