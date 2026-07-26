"""
===============================================================================
                        MIDDLE OF LINKED LIST
===============================================================================

Problem Statement
-----------------
Given the head of a singly linked list, return the middle node.

If the linked list has two middle nodes, return the SECOND middle node.

Example

Input

1 -> 2 -> 3 -> 4 -> 5

Output

3

-------------------------------------------------------------------------------
Pattern Learned ⭐⭐⭐
-------------------------------------------------------------------------------

Slow & Fast Pointer

-------------------------------------------------------------------------------
Intuition
-------------------------------------------------------------------------------

Approach 1 (Brute Force)

Find the length of the linked list.

Middle Index = Length // 2

Traverse again until the middle node.

---------------------------------------------------------

Approach 2 (Optimal)

Instead of counting nodes,

use two pointers.

• Slow moves one step.
• Fast moves two steps.

When Fast reaches the end,

Slow automatically reaches the middle.

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

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node

    def traverse(self):

        temp = self.head

        while temp:

            print(temp.data, end=" -> " if temp.next else "")
            temp = temp.next

        print()


# ============================================================================
# Solution
# ============================================================================


class Solution:

    # ------------------------------------------------------------------------
    # Brute Force
    # ------------------------------------------------------------------------

    def middle_brute(self, head):
        """
        Find the length first, then move to the middle node.
        """

        length = 0
        temp = head

        while temp:
            length += 1
            temp = temp.next

        middle = length // 2

        temp = head

        for _ in range(middle):
            temp = temp.next

        return temp

    # ------------------------------------------------------------------------
    # Optimal
    # ------------------------------------------------------------------------

    def middle_optimal(self, head):
        """
        Slow moves one step.
        Fast moves two steps.
        """

        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        return slow


# ============================================================================
# Driver Code
# ============================================================================

if __name__ == "__main__":

    ll = LinkedList()

    for value in [1, 2, 3, 4, 5, 6]:
        ll.insert_tail(value)

    print("Linked List")
    ll.traverse()

    solution = Solution()

    middle = solution.middle_brute(ll.head)
    print("\nMiddle (Brute Force):", middle.data)

    middle = solution.middle_optimal(ll.head)
    print("Middle (Optimal):", middle.data)


"""
===============================================================================
Dry Run (Optimal)

Input

1 -> 2 -> 3 -> 4 -> 5 -> 6

Initially

Slow
Fast

↓

1 -> 2 -> 3 -> 4 -> 5 -> 6

---------------------------------------------------------

Move

      Slow
            Fast

↓

1 -> 2 -> 3 -> 4 -> 5 -> 6

---------------------------------------------------------

Move

            Slow
                        Fast

↓

1 -> 2 -> 3 -> 4 -> 5 -> 6

---------------------------------------------------------

Move

                  Slow

↓

1 -> 2 -> 3 -> 4 -> 5 -> 6
                              Fast (None)

Loop Stops

Answer = 4

===============================================================================

Complexity
===============================================================================

Brute Force

Time  : O(n)
Space : O(1)

---------------------------------------------------------

Optimal

Time  : O(n)
Space : O(1)

Only one traversal is required.

===============================================================================

Interview Takeaway
===============================================================================

Pattern : Slow & Fast Pointer ⭐⭐⭐

Fast moves twice as fast as Slow.

When Fast reaches the end,

Slow automatically reaches the middle.

This same pattern is reused in:

• Detect Cycle
• Length of Cycle
• Starting Point of Cycle
• Palindrome Linked List

===============================================================================
"""
