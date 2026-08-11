"""
===============================================================================
                    REMOVE DUPLICATES FROM A SORTED DOUBLY LINKED LIST
===============================================================================

Problem
-------
Given the head of a SORTED Doubly Linked List, remove every duplicate node.

Example

Input
-----
1 <-> 2 <-> 2 <-> 2 <-> 3 <-> 4 <-> 4 <-> 5

Output
------
1 <-> 2 <-> 3 <-> 4 <-> 5

-------------------------------------------------------------------------------
Why is the word "SORTED" important?
-------------------------------------------------------------------------------

Since the list is sorted,

equal values always appear together.

Example

1 2 2 2 3 4 4 5

Instead of searching the entire list for duplicates,
we only need to remove consecutive duplicate nodes.

This immediately gives us an O(N) solution.

===============================================================================
PATTERN USED
===============================================================================

Anchor + Runner Pattern

Anchor (temp)
-------------
Keeps the FIRST occurrence.

Runner (next_node)
------------------
Moves ahead skipping every duplicate.

After skipping duplicates,

Anchor -----------------------> First Different Node

Reconnect them.

===============================================================================
QUICK CORE PSEUDOCODE (30 Seconds Revision)
===============================================================================

temp = head

while temp and temp.next

    next_node = temp.next

    while next_node and next_node.data == temp.data

        next_node = next_node.next

    temp.next = next_node

    if next_node
        next_node.prev = temp

    temp = temp.next

return head

===============================================================================
INTUITION
===============================================================================

Suppose

1 <-> 2 <-> 2 <-> 2 <-> 3

We keep

temp = first 2

Now move another pointer

next_node

until we find a value different from 2.

Eventually

next_node

points to

3

Now simply reconnect

2 ----------> 3

and

3 <---------- 2

All duplicate nodes disappear.

===============================================================================
DRY RUN
===============================================================================

Input

1 <-> 2 <-> 2 <-> 2 <-> 3 <-> 4 <-> 4 <-> 5

-------------------------------------------------
Iteration 1
-------------------------------------------------

temp = 1

next_node = 2

2 != 1

Nothing to remove.

Move temp.

1 <-> 2 <-> 2 <-> 2 <-> 3 <-> 4 <-> 4 <-> 5
      ^

-------------------------------------------------
Iteration 2
-------------------------------------------------

temp = first 2

next_node = second 2

Equal

Skip duplicate

next_node -> third 2

Still equal

Skip again

next_node -> 3

Now

Reconnect

temp.next = 3

3.prev = temp

List becomes

1 <-> 2 <-> 3 <-> 4 <-> 4 <-> 5

-------------------------------------------------
Iteration 3
-------------------------------------------------

temp = 3

No duplicate.

Move ahead.

-------------------------------------------------
Iteration 4
-------------------------------------------------

temp = first 4

Skip second 4

Reconnect with 5

Final

1 <-> 2 <-> 3 <-> 4 <-> 5

===============================================================================
WHY TWO WHILE LOOPS?
===============================================================================

Outer loop

Visits every DISTINCT value.

temp

↓

1

↓

2

↓

3

↓

4

↓

5

----------------------------------

Inner loop

Skips duplicates of ONE value.

2 -> 2 -> 2 -> 2

^^^^^^^^^^^^^^^^^

Skip all of them.

===============================================================================
TIME COMPLEXITY
===============================================================================

Outer loop

O(N)

Inner loop

Although nested,

every duplicate node is skipped only once.

Overall

O(N)

===============================================================================
SPACE COMPLEXITY
===============================================================================

O(1)

===============================================================================
"""


# =============================================================================
# Node Definition
# =============================================================================

class Node:
    """
    Represents one node of a Doubly Linked List.
    """

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# =============================================================================
# Solution
# =============================================================================

class Solution:
    """
    Removes duplicate nodes from a sorted doubly linked list.
    """

    def remove_duplicates(self, head: Node) -> Node:
        """
        Remove duplicate nodes from a sorted DLL.

        Parameters
        ----------
        head : Node
            Head of the doubly linked list.

        Returns
        -------
        Node
            Head of the modified linked list.

        Time Complexity
        ----------------
        O(N)

        Space Complexity
        -----------------
        O(1)
        """

        # Empty list or single node
        if head is None or head.next is None:
            return head

        # Anchor pointer
        temp = head

        # Visit every distinct value
        while temp and temp.next:

            # Runner starts from next node
            next_node = temp.next

            # ---------------------------------------------------------
            # Skip every duplicate of temp.data
            #
            # Example
            #
            # temp
            #  ↓
            # 2 -> 2 -> 2 -> 3
            #
            # Runner moves until value changes.
            # ---------------------------------------------------------

            while next_node and next_node.data == temp.data:
                next_node = next_node.next

            # ---------------------------------------------------------
            # Reconnect
            #
            # temp -----------> next_node
            # ---------------------------------------------------------

            temp.next = next_node

            # Fix backward pointer
            if next_node:
                next_node.prev = temp

            # Move to next distinct value
            temp = temp.next

        return head


# =============================================================================
# Helper Functions (For Learning)
# =============================================================================

def build_dll(values):
    """
    Builds a doubly linked list from a Python list.
    """

    if not values:
        return None

    head = Node(values[0])
    current = head

    for value in values[1:]:

        new_node = Node(value)

        current.next = new_node
        new_node.prev = current

        current = new_node

    return head


def print_dll(head):
    """
    Prints a doubly linked list.
    """

    current = head

    while current:

        print(current.data, end="")

        if current.next:
            print(" <-> ", end="")

        current = current.next

    print()


# =============================================================================
# Example Usage
# =============================================================================

if __name__ == "__main__":

    values = [1, 2, 2, 2, 3, 4, 4, 5]

    head = build_dll(values)

    print("Original DLL")
    print_dll(head)

    solution = Solution()

    head = solution.remove_duplicates(head)

    print("\nAfter Removing Duplicates")
    print_dll(head)

"""
Output

Original DLL
1 <-> 2 <-> 2 <-> 2 <-> 3 <-> 4 <-> 4 <-> 5

After Removing Duplicates
1 <-> 2 <-> 3 <-> 4 <-> 5
"""