"""
===============================================================================
                    DELETE THE MIDDLE NODE OF A LINKED LIST
===============================================================================

Problem Statement
-----------------
Given the head of a singly linked list, delete the middle node and return
the head of the modified linked list.

If there are two middle nodes, delete the SECOND middle node.

Example

Input

1 -> 2 -> 3 -> 4 -> 5

Output

1 -> 2 -> 4 -> 5

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

Traverse to the node just before the middle.

Reconnect the pointers.

---------------------------------------------------------

Approach 2 (Optimal)

Use Slow and Fast pointers.

Fast moves two steps.

Slow moves one step.

Keep another pointer (previous) behind Slow.

When Fast reaches the end,

Slow points to the middle node,

and Previous points to the node before it.

Delete the middle node by reconnecting:

previous.next = slow.next

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

    def delete_middle_brute(self, head):
        """
        Find the length first.

        Then remove the middle node.
        """

        if head is None or head.next is None:
            return None

        length = 0
        temp = head

        while temp:
            length += 1
            temp = temp.next

        middle = length // 2

        temp = head

        for _ in range(middle - 1):
            temp = temp.next

        temp.next = temp.next.next

        return head

    # ------------------------------------------------------------------------
    # Optimal
    # ------------------------------------------------------------------------

    def delete_middle(self, head):
        """
        Use Slow & Fast pointers.

        Keep a Previous pointer so that
        the middle node can be removed.
        """

        if head is None or head.next is None:
            return None

        slow = head
        fast = head
        previous = None

        while fast and fast.next:

            previous = slow
            slow = slow.next
            fast = fast.next.next

        previous.next = slow.next

        return head


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

    ll.head = solution.delete_middle(ll.head)

    print("\nAfter Deleting Middle Node")
    ll.traverse()


"""
===============================================================================
Dry Run (Optimal)

Input

1 -> 2 -> 3 -> 4 -> 5

Initially

Previous = None

Slow
Fast

↓

1 -> 2 -> 3 -> 4 -> 5

---------------------------------------------------------

Move

Previous

↓

1

Slow

↓

2

Fast

↓

3

---------------------------------------------------------

Move

Previous

↓

2

Slow

↓

3

Fast

↓

5

---------------------------------------------------------

Fast reached the end.

Previous points to 2.

Slow points to 3.

Delete

previous.next = slow.next

Result

1 -> 2 -> 4 -> 5

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

Slow finds the middle.

Previous keeps track of the node before the middle.

Reconnect the pointers to remove the middle node.

This problem is a direct extension of
"Middle of Linked List".

===============================================================================
"""