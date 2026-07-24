"""
===============================================================================
                    SORT 0s, 1s AND 2s
===============================================================================

Problem Statement
-----------------
Given the head of a linked list where each node contains only 0, 1 or 2,
sort the linked list in non-decreasing order.

Example

Input

1 -> 0 -> 2 -> 1 -> 0 -> 2 -> 1

Output

0 -> 0 -> 1 -> 1 -> 1 -> 2 -> 2

-------------------------------------------------------------------------------
Pattern Learned ⭐⭐⭐
-------------------------------------------------------------------------------

Multiple Dummy Nodes

-------------------------------------------------------------------------------
Intuition
-------------------------------------------------------------------------------

Instead of sorting, think of creating three separate linked lists.

Zero List

0 -> 0

One List

1 -> 1 -> 1

Two List

2 -> 2

Finally connect

Zero -> One -> Two

No new data nodes are created.
Only pointers are changed.

-------------------------------------------------------------------------------
Approach
-------------------------------------------------------------------------------

1. Create three Dummy Nodes.
2. Traverse the original list.
3. Append every node to its respective list.
4. Connect Zero -> One -> Two.
5. Return zero_head.next.

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

    def sort_012(self, head):
        """
        Sort a linked list containing only 0s, 1s and 2s.

        Returns:
            Head of the sorted linked list.
        """

        if head is None or head.next is None:
            return head

        zero_head = Node(-1)
        one_head = Node(-1)
        two_head = Node(-1)

        zero = zero_head
        one = one_head
        two = two_head

        temp = head

        while temp:

            if temp.data == 0:

                zero.next = temp
                zero = zero.next

            elif temp.data == 1:

                one.next = temp
                one = one.next

            else:

                two.next = temp
                two = two.next

            temp = temp.next

        # Connect the three lists

        zero.next = one_head.next if one_head.next else two_head.next

        one.next = two_head.next

        # Terminate the final list

        two.next = None

        return zero_head.next


# ============================================================================
# Driver Code
# ============================================================================

if __name__ == "__main__":

    ll = LinkedList()

    for value in [1, 0, 2, 1, 0, 2, 1]:
        ll.insert_tail(value)

    print("Original Linked List")
    ll.traverse()

    solution = Solution()

    ll.head = solution.sort_012(ll.head)

    print("\nSorted Linked List")
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

Only three Dummy Nodes are used.

===============================================================================
Interview Takeaway
===============================================================================

Pattern : Multiple Dummy Nodes ⭐⭐⭐

Instead of maintaining one chain,

maintain multiple chains.

Template

zero.next = node
zero = zero.next

one.next = node
one = one.next

two.next = node
two = two.next

Finally

Zero -> One -> Two

===============================================================================
"""