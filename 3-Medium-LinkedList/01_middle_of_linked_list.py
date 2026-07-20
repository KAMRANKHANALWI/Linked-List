"""
===============================================================================
                         MIDDLE OF LINKED LIST
===============================================================================

Problem Statement
-----------------
Given the head of a singly linked list, return the middle node.

If there are two middle nodes (even length list), return the SECOND middle node.

Example 1:
    Input:
        1 -> 2 -> 3 -> 4 -> 5

    Output:
        3


Example 2:
    Input:
        1 -> 2 -> 3 -> 4 -> 5 -> 6

    Output:
        4


===============================================================================
Intuition
===============================================================================

The first idea that comes to mind is:

    "Find the length first."

Once we know the length, we can calculate the middle index.

For example

Length = 5

Middle Index = 5 // 2 = 2

Move two steps from head.

Done.

Works perfectly.

But...

Can we do it in ONE traversal instead of TWO?

YES.

This is where the famous Slow & Fast Pointer technique comes in.

===============================================================================
Approach 1 : Brute Force (Two Traversals)
===============================================================================

Step 1:
    Count the number of nodes.

Step 2:
    middle = length // 2

Step 3:
    Traverse again until middle index.

Return that node.

Time Complexity:
    O(n) + O(n)
    = O(n)

Space Complexity:
    O(1)

===============================================================================
Approach 2 : Optimal (Slow & Fast Pointer)
===============================================================================

Idea:

Use two pointers.

slow moves ONE step.

fast moves TWO steps.

Visualization

Initial

1 -> 2 -> 3 -> 4 -> 5

S
F

--------------------------------

Move

1 -> 2 -> 3 -> 4 -> 5

     S
        F

--------------------------------

Move

1 -> 2 -> 3 -> 4 -> 5

          S
                F

--------------------------------

Fast reached the end.

Slow is exactly at the middle.

Why?

Because fast moves twice as quickly.

By the time fast covers the whole list,
slow has covered exactly half.

That's why slow lands in the middle.

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
    # Brute Force
    # -------------------------------------------------------------------------

    def middle_brute(self):

        # Count total nodes
        length = 0
        temp = self.head

        while temp:
            length += 1
            temp = temp.next

        middle = length // 2

        temp = self.head

        for _ in range(middle):
            temp = temp.next

        return temp

    # -------------------------------------------------------------------------
    # Optimal
    # -------------------------------------------------------------------------

    def middle_optimal(self):

        slow = self.head
        fast = self.head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        return slow


# =============================================================================
# Driver Code
# =============================================================================

if __name__ == "__main__":

    ll = LinkedList()

    ll.insert_tail(1)
    ll.insert_tail(2)
    ll.insert_tail(3)
    ll.insert_tail(4)
    ll.insert_tail(5)
    ll.insert_tail(6)

    print("Linked List:")
    ll.traverse()

    middle = ll.middle_brute()
    print("\nMiddle (Brute Force):", middle.data)

    middle = ll.middle_optimal()
    print("Middle (Optimal):", middle.data)


"""
===============================================================================
Dry Run (Optimal)

1 -> 2 -> 3 -> 4 -> 5 -> 6

S
F

--------------------------------

Move

1 -> 2 -> 3 -> 4 -> 5 -> 6

     S
        F

--------------------------------

Move

1 -> 2 -> 3 -> 4 -> 5 -> 6

          S
                F

--------------------------------

Move

1 -> 2 -> 3 -> 4 -> 5 -> 6

               S
                       F (None)

Loop Stops.

Answer = 4

===============================================================================
Time Complexity

Brute Force

O(n) + O(n)

Optimal

O(n)

===============================================================================
Space Complexity

Both

O(1)

===============================================================================
Takeaway:

Whenever a Linked List problem asks:

• middle node
• cycle detection
• palindrome
• kth node from end
• start of cycle

Think immediately about

    Slow Pointer
    Fast Pointer

===============================================================================
"""
