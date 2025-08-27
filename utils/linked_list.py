class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(values):
    """Builds a singly linked list from a list of values and returns the head."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    """Converts a singly linked list to a Python list of values."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result
