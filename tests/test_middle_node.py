import pytest
from solutions.middle_node import Solution

# Helper functions for linked list construction and conversion
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head

def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

@pytest.mark.parametrize(
    "input_list,expected_output",
    [
        pytest.param([1, 2, 3, 4, 5], [3, 4, 5], id="odd_length"),
        pytest.param([1, 2, 3, 4, 5, 6], [4, 5, 6], id="even_length"),
        pytest.param([1], [1], id="single_node"),
        pytest.param([1, 2], [2], id="two_nodes"),
        pytest.param([1, 2, 3], [2, 3], id="three_nodes"),
        pytest.param([10, 20, 30, 40, 50, 60, 70], [40, 50, 60, 70], id="longer_odd"),
        pytest.param([5, 6, 7, 8, 9, 10, 11, 12], [9, 10, 11, 12], id="longer_even"),
    ]
)
def test_middle_node_happy_path(input_list, expected_output):
    #
    # Arrange
    #
    s = Solution()
    head = build_linked_list(input_list)

    #
    # Act
    #
    middle = s.middleNode(head)

    #
    # Assert
    #
    assert linked_list_to_list(middle) == expected_output

@pytest.mark.parametrize(
    "input_list,expected_output",
    [
        pytest.param([], [], id="empty_list"),
    ]
)
def test_middle_node_edge_cases(input_list, expected_output):
    #
    # Arrange
    #
    s = Solution()
    head = build_linked_list(input_list)

    #
    # Act
    #
    middle = s.middleNode(head)

    #
    # Assert
    #
    assert linked_list_to_list(middle) == expected_output

@pytest.mark.parametrize(
    "input_list,expected_exception,case_id",
    [
        pytest.param(None, AttributeError, "none_head"),
    ]
)
def test_middle_node_error_cases(input_list, expected_exception, case_id):
    #
    # Arrange
    #
    s = Solution()

    #
    # Act & Assert
    #
    with pytest.raises(expected_exception):
        s.middleNode(input_list)
