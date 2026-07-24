"""
===============================================================================
                REVERSE LINKED LIST (RECURSIVE)
===============================================================================

Problem Statement
-----------------
Given the head of a singly linked list, reverse the linked list and
return the new head.

Example

Input

1 -> 2 -> 3 -> 4 -> 5

Output

5 -> 4 -> 3 -> 2 -> 1

-------------------------------------------------------------------------------
Pattern Learned ⭐⭐⭐
-------------------------------------------------------------------------------

Recursive Pointer Reversal

-------------------------------------------------------------------------------
Intuition
-------------------------------------------------------------------------------

Unlike the iterative approach, recursion first travels to the LAST node.

The last node automatically becomes the new head.

While the recursive calls return, we reverse each link one by one.

Think of recursion in two phases:

1. Going Down
   Reach the last node.

2. Coming Back
   Reverse every pointer.

-------------------------------------------------------------------------------
Approach
-------------------------------------------------------------------------------

1. Keep moving recursively until the last node.
2. The last node becomes the new head.
3. While returning:
       • Reverse the current link.
       • Break the old forward link.
4. Return the new head.

===============================================================================
"""


# ============================================================================
# Node
# ============================================================================

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# ============================================================================
# Linked List (Helper Class)
# ============================================================================

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_tail(self, data):
        """Insert a node at the end of the linked list."""

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node

    def traverse(self):
        """Print the linked list."""

        temp = self.head

        while temp:
            print(temp.data, end=" -> " if temp.next else "")
            temp = temp.next

        print()


# ============================================================================
# Solution
# ============================================================================

class Solution:

    def reverse(self, head):
        """
        Reverse a linked list recursively.

        Returns:
            New head of the reversed linked list.
        """

        return self._reverse(head)

    def _reverse(self, head):

        # Base Case
        if head is None or head.next is None:
            return head

        # Reverse the remaining list
        new_head = self._reverse(head.next)

        # Store the next node
        front = head.next

        # Reverse the current link
        front.next = head

        # Break the old link
        head.next = None

        return new_head


# ============================================================================
# Driver Code
# ============================================================================

if __name__ == "__main__":

    ll = LinkedList()

    for value in [1, 2, 3, 4, 5]:
        ll.insert_tail(value)

    print("Original Linked List")
    ll.traverse()

    solution = Solution()

    ll.head = solution.reverse(ll.head)

    print("\nReversed Linked List")
    ll.traverse()


"""
===============================================================================
Complexity
===============================================================================

Time Complexity

O(n)

Each node is visited exactly once.

Space Complexity

O(n)

Due to the recursion call stack.

===============================================================================
Interview Takeaway
===============================================================================

Pattern : Recursive Pointer Reversal ⭐⭐⭐

Recursion has two phases:

Going Down
    Reach the last node.

Coming Back
    Reverse every pointer.

Core Logic

    new_head = reverse(head.next)

    head.next.next = head
    head.next = None

    return new_head

Golden Rule

The recursive calls DO NOT reverse the list.

They only reach the last node.

The actual reversal happens while the recursion unwinds.

===============================================================================
"""