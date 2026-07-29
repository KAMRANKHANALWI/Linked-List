"""
===============================================================================
                    PALINDROME LINKED LIST
===============================================================================

Problem Statement
-----------------
Given the head of a singly linked list, determine whether the linked list
is a palindrome.

A palindrome reads the same forward and backward.

Return True if the linked list is a palindrome, otherwise return False.

Example 1

Input

1 -> 2 -> 2 -> 1

Output

True

Example 2

Input

1 -> 2 -> 3 -> 2 -> 1

Output

True

-------------------------------------------------------------------------------
Pattern Learned ⭐⭐⭐
-------------------------------------------------------------------------------

Pattern Composition

• Slow & Fast Pointer
• Pointer Reversal
• Two Pointer Comparison

-------------------------------------------------------------------------------
Intuition
-------------------------------------------------------------------------------

Approach 1 (Brute Force)

Store all node values inside an array.

Use two pointers to check whether the array is a palindrome.

---------------------------------------------------------

Approach 2 (Optimal)

Step 1

Find the middle of the linked list.

Step 2

Reverse the second half.

Step 3

Compare the first half and the reversed second half.

If every value matches,

the linked list is a palindrome.

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

    def is_palindrome_brute(self, head):
        """
        Store all node values inside an array.
        """

        values = []

        temp = head

        while temp:

            values.append(temp.data)
            temp = temp.next

        left = 0
        right = len(values) - 1

        while left < right:

            if values[left] != values[right]:
                return False

            left += 1
            right -= 1

        return True

    # ------------------------------------------------------------------------
    # Reverse Linked List
    # ------------------------------------------------------------------------

    def reverse(self, head):
        """
        Reverse a linked list and return the new head.
        """

        previous = None
        current = head

        while current:

            next_node = current.next

            current.next = previous

            previous = current
            current = next_node

        return previous

    # ------------------------------------------------------------------------
    # Optimal
    # ------------------------------------------------------------------------

    def is_palindrome(self, head):
        """
        Find the middle.

        Reverse the second half.

        Compare both halves.
        """

        if head is None or head.next is None:
            return True

        # Find middle
        slow = head
        fast = head

        while fast.next and fast.next.next:

            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        second_half = self.reverse(slow.next)

        # Compare both halves
        first = head
        second = second_half

        while second:

            if first.data != second.data:
                return False

            first = first.next
            second = second.next

        return True


# ============================================================================
# Driver Code
# ============================================================================

if __name__ == "__main__":

    ll = LinkedList()

    for value in [1, 2, 3, 2, 1]:
        ll.insert_tail(value)

    print("Linked List")
    ll.traverse()

    solution = Solution()

    print("\nIs Palindrome :", solution.is_palindrome(ll.head))


"""
===============================================================================
Dry Run (Optimal)

Input

1 -> 2 -> 3 -> 2 -> 1

Step 1

Find the middle.

1 -> 2 -> 3 -> 2 -> 1
          ↑
        Middle

---------------------------------------------------------

Step 2

Reverse the second half.

Original

2 -> 1

Reversed

1 -> 2

---------------------------------------------------------

Step 3

Compare

First Half

1 -> 2 -> 3

Second Half

1 -> 2

1 == 1 ✔

2 == 2 ✔

All nodes matched.

Answer = True

===============================================================================

Complexity
===============================================================================

Brute Force

Time  : O(n)

Space : O(n)

---------------------------------------------------------

Optimal

Time  : O(n)

Space : O(1)

===============================================================================

Interview Takeaway
===============================================================================

Pattern : Pattern Composition ⭐⭐⭐

This problem combines three patterns:

1. Slow & Fast Pointer
2. Pointer Reversal
3. Two Pointer Comparison

Instead of learning a new algorithm,

the interview tests whether you can combine
multiple patterns into one solution.

===============================================================================
"""