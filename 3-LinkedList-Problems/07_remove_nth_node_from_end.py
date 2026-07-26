"""
===============================================================================
                 REMOVE NTH NODE FROM END OF LIST
===============================================================================

Problem Statement
-----------------
Given the head of a singly linked list, remove the nth node from the end
of the list and return the head.

Example

Input

1 -> 2 -> 3 -> 4 -> 5

n = 2

Output

1 -> 2 -> 3 -> 5

-------------------------------------------------------------------------------
Pattern Learned ⭐⭐⭐
-------------------------------------------------------------------------------

Two Pointer Gap (Slow & Fast Pointer)

-------------------------------------------------------------------------------
Intuition
-------------------------------------------------------------------------------

Approach 1 (Brute Force)

If we know the length of the linked list,

Length = L

then

Nth node from end

=

(L - N)th node from the beginning.

Example

Length = 5

N = 2

Remove

5 - 2 = 3

Traverse to the node before it and reconnect the pointers.

---------------------------------------------------------

Approach 2 (Optimal)

Instead of calculating the length,

maintain a gap of N nodes between two pointers.

Step 1

Move Fast pointer N steps ahead.

Step 2

Move Slow and Fast together.

When Fast reaches the last node,

Slow will automatically be just before the node to delete.

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

    def remove_nth_from_end_brute(self, head, n):
        """
        Find the length first, then remove the required node.
        """

        if head is None:
            return None

        # Find length
        length = 0
        temp = head

        while temp:
            length += 1
            temp = temp.next

        # Delete head
        if length == n:
            return head.next

        # Position before the node to delete
        steps = length - n - 1

        temp = head

        while steps:

            temp = temp.next
            steps -= 1

        # Remove node
        temp.next = temp.next.next

        return head

    # ------------------------------------------------------------------------
    # Optimal
    # ------------------------------------------------------------------------

    def remove_nth_from_end(self, head, n):
        """
        Maintain a gap of n nodes between Fast and Slow.
        """

        if head is None:
            return None

        fast = head

        # Move Fast n steps ahead
        for _ in range(n):
            fast = fast.next

        # Head needs to be deleted
        if fast is None:
            return head.next

        slow = head

        # Maintain the gap
        while fast.next:

            slow = slow.next
            fast = fast.next

        # Delete node
        slow.next = slow.next.next

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

    ll.head = solution.remove_nth_from_end(ll.head, 2)

    print("\nAfter Removing 2nd Node From End")
    ll.traverse()


"""
===============================================================================
Dry Run (Optimal)

Input

1 -> 2 -> 3 -> 4 -> 5

n = 2

Step 1

Move Fast 2 steps.

Slow                 Fast
 ↓                    ↓
1 -> 2 -> 3 -> 4 -> 5

---------------------------------------------------------

Step 2

Move both together.

Slow                      Fast
 ↓                          ↓
2 -> 3 -> 4 -> 5

↓

Slow                          Fast
 ↓                              ↓
3 -> 4 -> 5

Fast reached the last node.

Slow is now just before the node to delete.

Delete

slow.next = slow.next.next

Result

1 -> 2 -> 3 -> 5

===============================================================================

Complexity
===============================================================================

Brute Force

Time Complexity

O(n)

Space Complexity

O(1)

---------------------------------------------------------

Optimal

Time Complexity

O(n)

Space Complexity

O(1)

The optimal approach performs the deletion in a single traversal.

===============================================================================

Interview Takeaway
===============================================================================

Pattern : Two Pointer Gap ⭐⭐⭐

Create a gap of N nodes.

Move both pointers together.

When Fast reaches the end,

Slow automatically reaches the node just before the one to delete.

This same idea appears in many Linked List problems involving
relative positions between two pointers.

===============================================================================
"""