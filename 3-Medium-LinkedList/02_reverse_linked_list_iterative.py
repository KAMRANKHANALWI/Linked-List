"""
===============================================================================
                  REVERSE LINKED LIST (ITERATIVE)
===============================================================================

Problem Statement
-----------------
Given the head of a singly linked list, reverse the linked list and
return the new head.

Example 1:

Input:
    1 -> 2 -> 3 -> 4 -> 5

Output:
    5 -> 4 -> 3 -> 2 -> 1


Example 2:

Input:
    1 -> 2

Output:
    2 -> 1


===============================================================================
Intuition
===============================================================================

Suppose we have

1 -> 2 -> 3 -> 4 -> 5 -> None

We want

5 -> 4 -> 3 -> 2 -> 1 -> None


Question:

Can we simply do

    current.next = previous

No.

Because the moment we change

1 -> 2

into

1 -> None

we lose access to

2 -> 3 -> 4 -> 5


So before changing any pointer,
we must SAVE the next node.

Golden Observation

Every iteration consists of only FOUR steps.

1. Save next node
2. Reverse current pointer
3. Move previous forward
4. Move current forward

These four steps repeat until the list ends.

===============================================================================
Approach 1 : Brute Force (Using Stack)
===============================================================================

Idea

Store all node values inside a stack.

Pop them one by one and overwrite the node values.

Example

Original

1 -> 2 -> 3

Stack

[1, 2, 3]

Pop

3

2

1

Now list becomes

3 -> 2 -> 1

Time Complexity

O(n)

Space Complexity

O(n)

Not preferred because it uses extra memory.

===============================================================================
Approach 2 : Optimal (Three Pointer Technique)
===============================================================================

Maintain three pointers.

previous
current
next_node

Initially

None <- 1 -> 2 -> 3 -> 4 -> 5

prev   curr


Step 1

Save next

next_node = current.next


Step 2

Reverse pointer

current.next = previous


Step 3

Move previous

previous = current


Step 4

Move current

current = next_node


Repeat until current becomes None.

Finally,

previous becomes the new head.

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
    # Reverse Linked List (Iterative)
    # -------------------------------------------------------------------------

    def reverse(self):

        previous = None
        current = self.head

        while current:

            # Save next node
            next_node = current.next

            # Reverse current pointer
            current.next = previous

            # Move previous one step
            previous = current

            # Move current one step
            current = next_node

        # previous becomes the new head
        self.head = previous


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

    print("Original Linked List")
    ll.traverse()

    ll.reverse()

    print("\nReversed Linked List")
    ll.traverse()


"""
===============================================================================
Dry Run

Original

1 -> 2 -> 3 -> None


Iteration 1

previous = None
current = 1

Save next

next_node = 2

Reverse

1 -> None

Move

previous = 1
current = 2


List

None <- 1

2 -> 3


------------------------------------------------------------

Iteration 2

Save next

next_node = 3

Reverse

2 -> 1

Move

previous = 2
current = 3


List

None <- 1 <- 2

3


------------------------------------------------------------

Iteration 3

Save next

next_node = None

Reverse

3 -> 2

Move

previous = 3
current = None


Loop Ends

New Head = previous

Final List

3 -> 2 -> 1

===============================================================================


Time Complexity

O(n)

Every node is visited exactly once.


Space Complexity

O(1)

No extra data structure is used.


===============================================================================
Interview Takeaway

Always remember these three pointers.

previous
current
next_node

Every iteration follows the exact same four steps.

1. Save next node
2. Reverse pointer
3. Move previous
4. Move current

This is one of the most important pointer manipulation patterns in
Linked Lists and appears in many interview questions.

===============================================================================
"""