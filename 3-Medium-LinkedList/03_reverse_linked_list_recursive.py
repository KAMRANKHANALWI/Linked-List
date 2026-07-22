"""
===============================================================================
                 REVERSE LINKED LIST (RECURSIVE)
===============================================================================

Golden Observation

The recursive calls only travel to the LAST node.

The actual reversal happens while recursion RETURNS.

Recursive Calls

reverse(1)
    reverse(2)
        reverse(3)
            reverse(4)
                reverse(5)

5 becomes the new head.

Then while returning,

5 -> 4

5 -> 4 -> 3

5 -> 4 -> 3 -> 2

5 -> 4 -> 3 -> 2 -> 1

===============================================================================
"""

# =============================================================================
# Node
# =============================================================================


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# =============================================================================
# Linked List
# =============================================================================


class LinkedList:

    def __init__(self):
        self.head = None

    # -------------------------------------------------------------------------
    # Insert at Tail
    # -------------------------------------------------------------------------

    def insert_tail(self, value):

        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node

    # -------------------------------------------------------------------------
    # Traverse
    # -------------------------------------------------------------------------

    def traverse(self):

        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # -------------------------------------------------------------------------
    # Reverse Recursively
    # -------------------------------------------------------------------------

    def reverse_recursive(self):

        self.head = self._reverse(self.head)

    # -------------------------------------------------------------------------
    # Helper Function
    # -------------------------------------------------------------------------

    def _reverse(self, head):

        # Base Case
        if head is None or head.next is None:
            return head

        # Reverse remaining list
        new_head = self._reverse(head.next)

        # Store next node
        front = head.next

        # Reverse link
        front.next = head

        # Break old link
        head.next = None

        # Return new head
        return new_head


# =============================================================================
# Driver Code
# =============================================================================

if __name__ == "__main__":

    ll = LinkedList()

    for value in [1, 2, 3, 4, 5]:
        ll.insert_tail(value)

    print("Original Linked List")
    ll.traverse()

    ll.reverse_recursive()

    print("\nReversed Linked List")
    ll.traverse()

