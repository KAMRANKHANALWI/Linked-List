"""
===============================================================================
                        REVERSE A DOUBLY LINKED LIST
===============================================================================

Problem Statement
-----------------
Given the head of a Doubly Linked List, reverse the list and return
the new head.

Example

Input

NULL <- 1 <-> 2 <-> 3 <-> 4 -> NULL

Output

NULL <- 4 <-> 3 <-> 2 <-> 1 -> NULL


===============================================================================
Golden Observation
===============================================================================

Unlike a Singly Linked List,

every node in a Doubly Linked List already stores BOTH directions.

        prev        next

NULL <- 2  <---->   3  <---->  4

To reverse the list,

we don't need complicated pointer manipulation.

For every node,

simply exchange

    prev

and

    next

That's it.

After every node swaps its two pointers,

the entire list becomes reversed.

The only remaining task is to find the new head.

===============================================================================
Quick Algorithm (30 Seconds)
===============================================================================

1. Start from head.

2. For every node

        swap(prev, next)

3. Move using current.prev

   (because after swapping,
    old next becomes prev)

4. Continue until current becomes NULL.

5. Return last.prev
   (or equivalently the last processed node)

===============================================================================
Quick Pseudo Code
===============================================================================

current = head

last = None

while current

    last = current.prev

    current.prev = current.next

    current.next = last

    current = current.prev

return last.prev

===============================================================================
Approach 1 : Brute Force (Using Stack)
===============================================================================

Idea

Traverse the DLL.

Store every value inside a stack.

Since stack is LIFO,

popping values automatically gives them
in reverse order.

Traverse the list again.

Replace node values using the popped values.

Notice

We are NOT reversing links.

We are only reversing DATA.

Time Complexity

O(n)

Space Complexity

O(n)

===============================================================================
Approach 2 : Optimal (Swap Pointers)
===============================================================================

Instead of reversing values,

reverse the LINKS.

For every node

swap

    prev

and

    next

Then move to

    current.prev

because

old next

became

new prev.

Finally,

return the new head.

Time Complexity

O(n)

Space Complexity

O(1)

===============================================================================
"""

# =============================================================================
# Node
# =============================================================================


class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# =============================================================================
# Doubly Linked List
# =============================================================================


class DoublyLinkedList:

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
        new_node.prev = temp

    # -------------------------------------------------------------------------
    # Traverse
    # -------------------------------------------------------------------------

    def traverse(self):

        temp = self.head

        while temp:

            print(temp.data, end=" <-> ")

            temp = temp.next

        print("None")

    # -------------------------------------------------------------------------
    # Brute Force
    # Reverse DATA using Stack
    # -------------------------------------------------------------------------

    def reverse_brute(self):

        stack = []

        temp = self.head

        # Step 1
        # Push every value

        while temp:

            stack.append(temp.data)

            temp = temp.next

        # Step 2
        # Replace values

        temp = self.head

        while temp:

            temp.data = stack.pop()

            temp = temp.next

    # -------------------------------------------------------------------------
    # Optimal
    # Reverse LINKS
    # -------------------------------------------------------------------------

    def reverse_optimal(self):

        if self.head is None:
            return

        current = self.head
        last = None

        while current:

            # Save old previous

            last = current.prev

            # Swap pointers

            current.prev = current.next
            current.next = last

            # Move forward
            # (old next became prev)

            current = current.prev

        # last currently points to
        # previous pointer of original tail

        self.head = last.prev


# =============================================================================
# Driver Code
# =============================================================================

if __name__ == "__main__":

    dll = DoublyLinkedList()

    dll.insert_tail(1)
    dll.insert_tail(2)
    dll.insert_tail(3)
    dll.insert_tail(4)

    print("Original DLL")
    dll.traverse()

    print("\nReverse using Stack")
    dll.reverse_brute()
    dll.traverse()

    print("\nReverse again using Pointer Swapping")
    dll.reverse_optimal()
    dll.traverse()


"""
===============================================================================
Dry Run (Optimal)

Original

NULL <- 1 <-> 2 <-> 3 <-> 4 -> NULL


--------------------------------

Current = 1

prev = NULL

next = 2

Swap

prev = 2

next = NULL

Move

current = 2


--------------------------------

Current = 2

prev = 3

next = 1

Move

current = 3


--------------------------------

Current = 3

prev = 4

next = 2

Move

current = 4


--------------------------------

Current = 4

prev = NULL

next = 3

Move

current = NULL

Loop Ends.

New Head = 4

===============================================================================
Mental Checklist
===============================================================================

✓ Every node swaps

        prev

and

        next

✓ Move using

        current.prev

NOT

        current.next

✓ Update head at the end

===============================================================================
Common Mistakes
===============================================================================

❌ Moving using current.next

After swapping,

next points backward.

Always move using

current.prev.

--------------------------------

❌ Forgetting to update head

After reversing,

the original tail becomes the new head.

--------------------------------

❌ Reversing only next pointer

Both

prev

and

next

must be swapped.

===============================================================================
Pattern Recognition
===============================================================================

Singly Linked List

Reverse

        next

pointer only.

--------------------------------

Doubly Linked List

Swap

        prev

and

        next

for every node.

===============================================================================
Related Problems
===============================================================================

✓ Reverse Linked List

✓ Reverse Doubly Linked List

✓ Reverse Nodes in K Group

✓ Flatten Doubly Linked List

✓ Browser History (DLL)

===============================================================================
Takeaway
===============================================================================

The biggest realization is:

A Doubly Linked List already stores both directions.

Reversing it is simply exchanging those directions.

Remember one sentence:

    "Swap prev and next for every node."

Everything else follows naturally.

===============================================================================
"""