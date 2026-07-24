"""
===============================================================================
                      ODD EVEN LINKED LIST
===============================================================================

Problem Statement
-----------------
Given the head of a singly linked list, group all the nodes at odd positions
together followed by the nodes at even positions.

The relative order inside both groups should remain the same.

Example

Input

1 -> 2 -> 3 -> 4 -> 5

Output

1 -> 3 -> 5 -> 2 -> 4

-------------------------------------------------------------------------------
Pattern Learned ⭐⭐⭐
-------------------------------------------------------------------------------

Pointer Manipulation

-------------------------------------------------------------------------------
Intuition
-------------------------------------------------------------------------------

Instead of rearranging one linked list, think of splitting it into two chains:

Odd Chain

1 -> 3 -> 5

Even Chain

2 -> 4

Maintain three pointers:

• odd
• even
• even_head

Build both chains simultaneously and finally connect

odd.next = even_head

-------------------------------------------------------------------------------
Approach
-------------------------------------------------------------------------------

1. Initialize odd, even and even_head.
2. Skip alternate nodes to build odd and even chains.
3. Move odd and even pointers forward.
4. Connect the odd chain with the even chain.
5. Return the original head.

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

    def odd_even_list(self, head):
        """
        Rearrange nodes so that all odd-position nodes come first,
        followed by all even-position nodes.
        """

        # Empty list or only one node
        if head is None or head.next is None:
            return head

        odd = head
        even = head.next

        # Save the beginning of the even chain
        even_head = even

        while even and even.next:

            # Connect current odd node to the next odd node
            odd.next = odd.next.next

            # Move odd forward
            odd = odd.next

            # Connect current even node to the next even node
            even.next = even.next.next

            # Move even forward
            even = even.next

        # Join odd chain with even chain
        odd.next = even_head

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

    ll.head = solution.odd_even_list(ll.head)

    print("\nOdd Even Linked List")
    ll.traverse()


"""
===============================================================================
Complexity
===============================================================================

Time Complexity

O(n)

Each node is visited only once.

Space Complexity

O(1)

Only three pointers are used.

===============================================================================
Interview Takeaway
===============================================================================

Pattern : Pointer Manipulation ⭐⭐⭐

We are NOT creating new nodes.

We are NOT deleting nodes.

We are simply reconnecting pointers to form two separate chains.

Pointers Used

odd        -> Traverses odd-position nodes

even       -> Traverses even-position nodes

even_head  -> Stores the start of the even chain

Golden Pattern

while even and even.next:

    odd.next = odd.next.next
    odd = odd.next

    even.next = even.next.next
    even = even.next

odd.next = even_head

===============================================================================
"""
