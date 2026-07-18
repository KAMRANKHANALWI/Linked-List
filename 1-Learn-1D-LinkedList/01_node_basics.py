"""
===============================================================================
                            LINKED LIST - NODE BASICS
===============================================================================

-------------------------------------------------------------------------------
What is a Node?
-------------------------------------------------------------------------------

A Node is the smallest building block of a Linked List.

Every node stores two things:

    1. Data
    2. Reference to the next node

Visual Representation

        +----------------------+
        | data = 10            |
        | next = Reference ----|------>
        +----------------------+

Notice:

The next field DOES NOT store the next value.

Wrong

    next = 20

Correct

    next = Reference to Node(20)

-------------------------------------------------------------------------------
How does a Linked List look?
-------------------------------------------------------------------------------

Head

  |
  v

+--------+     +--------+     +--------+
|  10    | --> |  20    | --> |  30    | --> None
+--------+     +--------+     +--------+

Every arrow represents an OBJECT REFERENCE.

Nodes are NOT stored continuously in memory.

Python automatically stores objects wherever memory is available.

The references connect them together.

===============================================================================
"""


class Node:
    """
    Represents a single node of a Singly Linked List.

    Attributes
    ----------
    data : Any
        Stores the actual value.

    next : Node | None
        Stores a reference to the next node.

        Initially None because the node
        is not connected to anything.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


# =============================================================================
# Creating Individual Nodes
# =============================================================================

first = Node(10)
second = Node(20)
third = Node(30)
fourth = Node(40)
fifth = Node(50)

# At this moment the nodes are NOT connected.

#
# first
#
#    10
#
# second
#
#    20
#
# third
#
#    30
#


# =============================================================================
# Connecting Nodes
# =============================================================================

first.next = second
second.next = third
third.next = fourth
fourth.next = fifth

#
# first
#   |
#   v
#
# 10 ----> 20 ----> 30 ----> 40 ----> 50 ----> None
#


# =============================================================================
# Accessing Data
# =============================================================================

print("First Node :", first.data)

print("Second Node:", first.next.data)

print("Third Node :", first.next.next.data)

print("Fourth Node:", first.next.next.next.data)

print("Fifth Node :", first.next.next.next.next.data)


# =============================================================================
# Understanding References
# =============================================================================

"""
Suppose we execute

temp = first

Does Python create another node?

NO.

Memory now looks like

        first
          |
          |
          V

       +--------+
       |   10   |
       +--------+
          ^
          |
        temp

Both variables point to the SAME object.
"""

temp = first

print(temp.data)

# Changing data using temp

temp.data = 100

print(first.data)

"""
Output

100

Why?

Because

temp

and

first

refer to the SAME object.
"""


# =============================================================================
# Another Example
# =============================================================================

another = first

another.data = 999

print(first.data)

"""
Output

999

Again,

No new node was created.

Only another reference was added.
"""


# =============================================================================
# Key Takeaways
# =============================================================================

"""
1. Variables DO NOT store nodes.

2. Variables store REFERENCES to nodes.

3. A Node stores:

       data
       next

4. next stores a REFERENCE,
   not the next value.

5. Multiple variables can point
   to the same node.

6. Changing a node through one
   reference affects every other
   reference pointing to that node.

This single concept is the foundation
of every Linked List problem.
"""