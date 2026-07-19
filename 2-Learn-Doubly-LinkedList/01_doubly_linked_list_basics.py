"""
===============================================================================
                    DOUBLY LINKED LIST - NODE BASICS
===============================================================================

Goal:
    Understand what a Doubly Linked List is and how it differs from a
    Singly Linked List.

Difference:

    Singly Node
        data + next

    Doubly Node
        data + prev + next

A Doubly Linked List allows traversal in both directions.

Visualization:

    None <- 10 <-> 20 <-> 30 -> None

Every node stores:
    1. Data
    2. Reference to previous node
    3. Reference to next node

===============================================================================
"""

# =============================================================================
# Node
# =============================================================================


class Node:
    """
    Represents one node of a Doubly Linked List.

    Attributes
    ----------
    data : Any
        Value stored in the node.

    prev : Node | None
        Reference to previous node.

    next : Node | None
        Reference to next node.
    """

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# =============================================================================
# Creating Individual Nodes
# =============================================================================

first = Node(10)
second = Node(20)
third = Node(30)
fourth = Node(40)
fifth = Node(50)

# =============================================================================
# Connecting Nodes
# =============================================================================

# 10 <-> 20
first.next = second
second.prev = first

# 20 <-> 30
second.next = third
third.prev = second

# 30 <-> 40
third.next = fourth
fourth.prev = third

# 40 <-> 50
fourth.next = fifth
fifth.prev = fourth

"""
Final Structure

None <- 10 <-> 20 <-> 30 <-> 40 <-> 50 -> None
"""


# =============================================================================
# Traversing Forward
# =============================================================================

print("Forward Traversal")

temp = first

while temp:
    print(temp.data, end=" <-> ")
    temp = temp.next

print("None")


# =============================================================================
# Traversing Backward
# =============================================================================

print("\nBackward Traversal")

temp = fifth

while temp:
    print(temp.data, end=" <-> ")
    temp = temp.prev

print("None")


# =============================================================================
# Understanding References
# =============================================================================

"""
Suppose

temp = third

Memory

10 <-> 20 <-> 30 <-> 40 <-> 50
              ^
              |
            temp

Move Forward

temp = temp.next

10 <-> 20 <-> 30 <-> 40 <-> 50
                     ^
                     |
                   temp

Move Backward

temp = temp.prev

10 <-> 20 <-> 30 <-> 40 <-> 50
              ^
              |
            temp

Notice:

Nodes never move.

Only the reference stored in 'temp' moves.
"""

temp = third

print("\nCurrent :", temp.data)

temp = temp.next
print("Next    :", temp.data)

temp = temp.prev
print("Previous:", temp.data)


# =============================================================================
# Accessing Neighbours
# =============================================================================

print("\nCurrent Node :", third.data)
print("Previous Node:", third.prev.data)
print("Next Node    :", third.next.data)


# =============================================================================
# Key Takeaways
# =============================================================================

"""
1. A Doubly Linked List node stores:
       data
       prev
       next

2. Every connection requires TWO updates.

       first.next = second
       second.prev = first

3. Forward Traversal

       temp = temp.next

4. Backward Traversal

       temp = temp.prev

5. Nodes never move.
   Only references move.

6. Compared to Singly Linked List,
   a Doubly Linked List uses extra memory
   but allows traversal in both directions.
"""
