"""
===============================================================================
                            ADD TWO NUMBERS
===============================================================================

Problem Statement
-----------------
You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order, and each node contains a
single digit.

Add the two numbers and return the sum as a linked list.

Example

L1 : 2 -> 4 -> 3
L2 : 5 -> 6 -> 4

342 + 465 = 807

Answer

7 -> 0 -> 8

-------------------------------------------------------------------------------
Pattern Learned ⭐⭐⭐
-------------------------------------------------------------------------------

Dummy Node

Whenever a Linked List problem asks you to BUILD a NEW linked list,
think immediately about using a Dummy Node.

-------------------------------------------------------------------------------
Intuition
-------------------------------------------------------------------------------

The challenge is not the addition.

The challenge is building the answer linked list.

Without a Dummy Node, the first node has to be handled separately.

    head = new_node

while every remaining node uses

    current.next = new_node

A Dummy Node removes this special case.

We simply keep attaching new nodes after 'current' and finally return

    dummy.next

-------------------------------------------------------------------------------
Approach
-------------------------------------------------------------------------------

1. Create a Dummy Node.
2. Maintain a pointer 'current' to build the answer list.
3. Traverse both linked lists together.
4. Add current digits along with carry.
5. Store digit = total % 10.
6. Update carry = total // 10.
7. Attach the new digit after current.
8. Move current forward.
9. If one carry remains, create one last node.
10. Return dummy.next.

===============================================================================
"""

# ============================================================================
# Node Definition
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
# Optimal Solution
# ============================================================================


def add_two_numbers(head1, head2):
    """
    Adds two numbers represented as linked lists.

    Time Complexity : O(max(N, M))
    Space Complexity : O(max(N, M))
    """

    dummy = Node(-1)
    current = dummy

    carry = 0

    t1 = head1
    t2 = head2

    while t1 or t2:

        total = carry

        if t1:
            total += t1.data
            t1 = t1.next

        if t2:
            total += t2.data
            t2 = t2.next

        digit = total % 10
        carry = total // 10

        current.next = Node(digit)
        current = current.next

    if carry:
        current.next = Node(carry)

    return dummy.next


# ============================================================================
# Driver Code
# ============================================================================

list1 = LinkedList()

for value in [2, 4, 3]:
    list1.insert_tail(value)

print("Number 1:")
list1.traverse()


list2 = LinkedList()

for value in [5, 6, 4]:
    list2.insert_tail(value)

print("Number 2:")
list2.traverse()


answer_head = add_two_numbers(list1.head, list2.head)

answer = LinkedList()
answer.head = answer_head

print("Sum:")
answer.traverse()


"""
===============================================================================
Dry Run
===============================================================================

L1 : 2 -> 4 -> 3
L2 : 5 -> 6 -> 4

carry = 0

--------------------------------

2 + 5 + 0 = 7

digit = 7

carry = 0

Answer

7

--------------------------------

4 + 6 + 0 = 10

digit = 0

carry = 1

Answer

7 -> 0

--------------------------------

3 + 4 + 1 = 8

digit = 8

carry = 0

Answer

7 -> 0 -> 8

Return

dummy.next

===============================================================================
Complexity
===============================================================================

Time Complexity

O(max(N, M))

Space Complexity

O(max(N, M))

===============================================================================
Interview Takeaway
===============================================================================

Pattern : Dummy Node ⭐⭐⭐

Whenever a problem asks you to BUILD a new Linked List,

use

    dummy = Node(-1)
    current = dummy

Attach every new node using

    current.next = Node(value)
    current = current.next

Finally return

    dummy.next

Problems using the same pattern

✓ Merge Two Sorted Lists
✓ Merge K Sorted Lists
✓ Partition List
✓ Remove Elements
✓ Swap Nodes in Pairs

===============================================================================
"""
