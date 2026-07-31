"""
===============================================================================
                            ADD ONE TO A NUMBER
===============================================================================

Problem Statement
-----------------
A non-negative integer is represented as a singly linked list where each node
contains a single digit.

Add one to the number and return the updated head.

Example 1
---------
Input : 1 -> 5 -> 9
Output: 1 -> 6 -> 0

Example 2
---------
Input : 9 -> 9 -> 9
Output: 1 -> 0 -> 0 -> 0

===============================================================================
Notebook Notes
===============================================================================

Key Observation
---------------
Addition always starts from the LAST digit.

Linked Lists only allow forward traversal.

So we need a way to process the list from right to left.

There are two elegant approaches.

1. Reverse → Add One → Reverse Back
2. Recursion (process while returning)

We'll implement both.

===============================================================================
Approach 1 : Reverse the List
===============================================================================

Idea
----
Reverse the list so the least significant digit comes first.

Example

1 -> 5 -> 9

Reverse

9 -> 5 -> 1

Now simply add one like normal addition.

If carry still exists after the loop,
create a new node.

Finally reverse the list again.

Pattern
-------
Pointer Reversal

Time Complexity : O(n)
Space Complexity: O(1)

===============================================================================
Approach 2 : Recursion (Optimal)
===============================================================================

Idea
----
Recursion naturally reaches the last node first.

While returning,
each node receives the carry from its next node.

Example

1 -> 9 -> 9

Travel

1
↓
9
↓
9

Return

9 + 1 = 10
Store 0
Carry = 1

↓

9 + 1 = 10
Store 0
Carry = 1

↓

1 + 1 = 2
Carry = 0

Result

2 -> 0 -> 0

Pattern
-------
Recursion / Backtracking

Time Complexity : O(n)
Space Complexity: O(n)   (Recursion Stack)

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
# Linked List
# ============================================================================


class LinkedList:

    def __init__(self):
        self.head = None

    # ------------------------------------------------------------------------
    # Insert at Tail
    # ------------------------------------------------------------------------

    def insert_tail(self, value):

        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node

    # ------------------------------------------------------------------------
    # Traverse
    # ------------------------------------------------------------------------

    def traverse(self):

        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # ------------------------------------------------------------------------
    # Reverse Linked List
    # ------------------------------------------------------------------------

    def reverse(self, head):

        prev = None
        curr = head

        while curr:

            front = curr.next
            curr.next = prev
            prev = curr
            curr = front

        return prev

    # ------------------------------------------------------------------------
    # Approach 1 : Reverse Twice
    # ------------------------------------------------------------------------

    def add_one_reverse(self):

        head = self.reverse(self.head)

        temp = head
        carry = 1

        while temp:

            temp.data += carry

            if temp.data < 10:
                carry = 0
                break

            temp.data = 0
            carry = 1

            if temp.next is None:
                break

            temp = temp.next

        if carry == 1:

            new_node = Node(1)
            head = self.reverse(head)

            new_node.next = head
            self.head = new_node

        else:

            self.head = self.reverse(head)

    # ------------------------------------------------------------------------
    # Recursive Helper
    # ------------------------------------------------------------------------

    def helper(self, node):

        if node is None:
            return 1

        carry = self.helper(node.next)

        node.data += carry

        if node.data < 10:
            return 0

        node.data = 0
        return 1

    # ------------------------------------------------------------------------
    # Approach 2 : Recursion
    # ------------------------------------------------------------------------

    def add_one_recursive(self):

        carry = self.helper(self.head)

        if carry:

            new_head = Node(1)
            new_head.next = self.head
            self.head = new_head


# ============================================================================
# Driver Code
# ============================================================================

if __name__ == "__main__":

    ll = LinkedList()

    for value in [9, 9, 9]:
        ll.insert_tail(value)

    print("Original Number")
    ll.traverse()

    ll.add_one_reverse()

    print("\nAfter Reverse Method")
    ll.traverse()

    ll2 = LinkedList()

    for value in [9, 9, 9]:
        ll2.insert_tail(value)

    ll2.add_one_recursive()

    print("\nAfter Recursive Method")
    ll2.traverse()


"""
===============================================================================
Dry Run (Recursive)

Input

9 -> 9 -> 9

Travel

9
↓
9
↓
9

Return

Last

9 + 1 = 10

Store 0
Carry = 1

↓

Middle

9 + 1 = 10

Store 0
Carry = 1

↓

Head

9 + 1 = 10

Store 0
Carry = 1

Carry still exists

Create new node

1 -> 0 -> 0 -> 0

===============================================================================
Revision Box
===============================================================================

✔ Reverse Method
    Reverse → Add One → Reverse

✔ Recursive Method
    Process from the last node while recursion returns.

Patterns Learned

• Pointer Reversal
• Recursion / Backtracking
• Carry Propagation

===============================================================================
"""
