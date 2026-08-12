"""
============================================================
Problem: Rotate Linked List
============================================================

Problem Statement
-----------------
Given the head of a linked list and an integer k,
rotate the linked list to the right by k positions.

A right rotation means moving the last node
to the front of the list.

Example

Input

1 → 2 → 3 → 4 → 5

k = 2

Output

4 → 5 → 1 → 2 → 3

------------------------------------------------------------
Golden Observation
------------------------------------------------------------

Instead of physically moving the last node K times,
notice that after every 'length' rotations,
the list becomes exactly the same.

Therefore,

    k = k % length

Now another important observation:

Instead of moving nodes one by one,

1. Convert the linked list into a circular linked list.
2. Find the new last node.
3. Break the circle.

That's all.

------------------------------------------------------------
Intuition
------------------------------------------------------------

Example

1 → 2 → 3 → 4 → 5

Rotate by 2

The last two nodes

4 → 5

should come in front.

Think of the list as

1 → 2 → 3 | 4 → 5

Instead of cutting and reconnecting manually,

make it circular

1 → 2 → 3 → 4 → 5
↑                 |
|_________________|

Now simply decide

where should the new head be?

Length = 5

K = 2

New Head starts after

Length - K

= 3rd node

So

newLastNode = 3

head = 4

Finally,

break the circle after node 3.

Done.

------------------------------------------------------------
Pseudo Code
------------------------------------------------------------

Find Length
Find Tail

k = k % length

If k == 0
    return head

Connect Tail to Head

Find (length-k)th node

New Head = next of this node

Break the circle

Return head
"""

# ==========================================================
# Node Definition
# ==========================================================


class Node:
    """
    Node of a Singly Linked List.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


# ==========================================================
# Helper Function
# Find the nth node (1-indexed)
# ==========================================================


def find_nth_node(head, n):
    """
    Returns the nth node of the linked list.

    Example

    1 → 2 → 3 → 4 → 5

    n = 3

    returns node containing 3

    Time : O(n)
    """

    count = 1
    current = head

    while current:

        if count == n:
            return current

        count += 1
        current = current.next

    return None


# ==========================================================
# Main Function
# ==========================================================


def rotate_right(head, k):
    """
    Rotates the linked list to the right by k positions.

    Time  : O(N)
    Space : O(1)
    """

    # Empty list or no rotation
    if head is None or k == 0:
        return head

    # ------------------------------------------------------
    # Step 1
    # Find Length and Tail
    # ------------------------------------------------------

    length = 1
    tail = head

    while tail.next:
        tail = tail.next
        length += 1

    # ------------------------------------------------------
    # Step 2
    # Normalize K
    # ------------------------------------------------------

    k = k % length

    if k == 0:
        return head

    # ------------------------------------------------------
    # Step 3
    # Convert into Circular Linked List
    # ------------------------------------------------------

    tail.next = head

    # ------------------------------------------------------
    # Step 4
    # Find the New Last Node
    #
    # New Last Node = (length-k)th node
    # ------------------------------------------------------

    new_last_node = find_nth_node(head, length - k)

    # ------------------------------------------------------
    # Step 5
    # New Head is next node
    # ------------------------------------------------------

    new_head = new_last_node.next

    # ------------------------------------------------------
    # Step 6
    # Break the Circle
    # ------------------------------------------------------

    new_last_node.next = None

    return new_head


# ==========================================================
# Utility Functions
# ==========================================================


def build_linked_list(values):
    """Builds a linked list from a Python list."""

    if not values:
        return None

    head = Node(values[0])
    current = head

    for value in values[1:]:
        current.next = Node(value)
        current = current.next

    return head


def print_linked_list(head):
    """Prints the linked list."""

    current = head

    while current:
        print(current.data, end=" -> " if current.next else "")
        current = current.next

    print()


# ==========================================================
# Driver Code
# ==========================================================

head = build_linked_list([1, 2, 3, 4, 5])

print("Original Linked List")
print_linked_list(head)

head = rotate_right(head, 2)

print("\nAfter Rotating by 2")
print_linked_list(head)

"""
Output

Original Linked List

1 -> 2 -> 3 -> 4 -> 5

After Rotation

4 -> 5 -> 1 -> 2 -> 3
"""

# ==========================================================
# Dry Run
# ==========================================================

"""
Input

1 → 2 → 3 → 4 → 5

K = 2

---------------------------------

Length = 5

Tail = 5

---------------------------------

k = k % length

k = 2

---------------------------------

Create Circle

1 → 2 → 3 → 4 → 5
↑                 |
|_________________|

---------------------------------

Find

length-k

5-2

=

3

Third node

↓

3

---------------------------------

New Head

↓

4

---------------------------------

Break

3.next = NULL

Final

4 → 5 → 1 → 2 → 3
"""

# ==========================================================
# Complexity Analysis
# ==========================================================

"""
Time Complexity
---------------

Finding Length        : O(N)

Finding New Last Node : O(N)

Overall

O(N)

-----------------------------------

Space Complexity

O(1)

Only a few pointers are used.

-----------------------------------

Key Interview Takeaways

✓ Rotating by Length times changes nothing.

✓ Always reduce

    k = k % length

✓ Convert the list into a circle.

✓ New Last Node is always

    (Length - K)th node

✓ New Head is simply

    newLastNode.next

✓ Break the circle.

This is the cleanest O(N) solution.
"""
