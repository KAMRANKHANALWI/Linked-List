"""
===============================================================================
                REVERSE LINKED LIST (ITERATIVE)
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

Three Pointer Reversal

-------------------------------------------------------------------------------
Intuition
-------------------------------------------------------------------------------

Reversing a linked list is simply reversing every pointer.

The only challenge is that changing

    current.next = previous

would make us lose the remaining list.

So before reversing any pointer, we first save the next node.

Every iteration follows the same four steps:

1. Save next node
2. Reverse current pointer
3. Move previous forward
4. Move current forward

-------------------------------------------------------------------------------
Approach
-------------------------------------------------------------------------------

1. Initialize:
       previous = None
       current = head

2. Repeat until current becomes None:
       • Save next node
       • Reverse pointer
       • Move previous
       • Move current

3. previous becomes the new head.

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
        Reverse a singly linked list.

        Returns:
            New head of the reversed linked list.
        """

        previous = None
        current = head

        while current:

            # Step 1 : Save next node
            next_node = current.next

            # Step 2 : Reverse pointer
            current.next = previous

            # Step 3 : Move previous
            previous = current

            # Step 4 : Move current
            current = next_node

        return previous


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

O(1)

No extra data structure is used.

===============================================================================
Interview Takeaway
===============================================================================

Pattern : Three Pointer Reversal ⭐⭐⭐

Whenever you need to reverse a linked list, remember:

    previous = None
    current = head

    while current:

        next_node = current.next
        current.next = previous

        previous = current
        current = next_node

    return previous

Golden Rule

Never reverse a pointer before saving the next node.

Think:

    Save
      ↓
    Reverse
      ↓
    Move Previous
      ↓
    Move Current

===============================================================================
"""