"""
===============================================================================
                    MERGE TWO SORTED LISTS
===============================================================================

Problem Statement
-----------------
You are given the heads of two sorted linked lists.

Merge them into one sorted linked list and return its head.

The merged list should also be sorted.

Example

List 1

1 -> 2 -> 4

List 2

1 -> 3 -> 4

Output

1 -> 1 -> 2 -> 3 -> 4 -> 4

-------------------------------------------------------------------------------
Pattern Learned ⭐⭐⭐
-------------------------------------------------------------------------------

Dummy Node

-------------------------------------------------------------------------------
Intuition
-------------------------------------------------------------------------------

Both linked lists are already sorted.

At every step, simply choose the smaller node and attach it to the
answer list.

Instead of handling the first node separately, use a Dummy Node.

This allows us to build the answer list without any special cases.

-------------------------------------------------------------------------------
Approach
-------------------------------------------------------------------------------

1. Create a Dummy Node.
2. Maintain a 'current' pointer.
3. Compare the current nodes of both lists.
4. Attach the smaller node.
5. Move the corresponding pointer forward.
6. Repeat until one list finishes.
7. Attach the remaining nodes.
8. Return dummy.next.

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

    def merge_two_lists(self, head1, head2):
        """
        Merge two sorted linked lists.

        Returns:
            Head of the merged sorted linked list.
        """

        dummy = Node(-1)
        current = dummy

        t1 = head1
        t2 = head2

        while t1 and t2:

            if t1.data <= t2.data:

                current.next = t1
                t1 = t1.next

            else:

                current.next = t2
                t2 = t2.next

            current = current.next

        # Attach the remaining nodes

        if t1:
            current.next = t1

        if t2:
            current.next = t2

        return dummy.next


# ============================================================================
# Driver Code
# ============================================================================

if __name__ == "__main__":

    list1 = LinkedList()

    for value in [1, 2, 4]:
        list1.insert_tail(value)

    print("List 1")
    list1.traverse()

    list2 = LinkedList()

    for value in [1, 3, 4]:
        list2.insert_tail(value)

    print("\nList 2")
    list2.traverse()

    solution = Solution()

    merged_head = solution.merge_two_lists(list1.head, list2.head)

    merged = LinkedList()
    merged.head = merged_head

    print("\nMerged List")
    merged.traverse()


"""
===============================================================================
Complexity
===============================================================================

Time Complexity

O(n + m)

Every node is visited exactly once.

Space Complexity

O(1)

No extra linked list is created.
Only one Dummy Node is used.

===============================================================================
Interview Takeaway
===============================================================================

Pattern : Dummy Node ⭐⭐⭐

Notice the difference from Add Two Numbers.

Add Two Numbers

    Create NEW nodes.

Merge Two Sorted Lists

    Reuse EXISTING nodes.

Both problems use the same Dummy Node pattern.

Template

    dummy = Node(-1)
    current = dummy

    while ...:

        current.next = ...
        current = current.next

    current.next = remaining_nodes

    return dummy.next

===============================================================================
"""

