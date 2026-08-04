"""
===============================================================================
                  DELETE ALL OCCURRENCES OF A KEY IN DLL
===============================================================================

Problem Statement
-----------------
Given the head of a Doubly Linked List and an integer key,
delete EVERY node whose value equals the given key.

Return the new head.

Example

Input

NULL <- 4 <-> 10 <-> 6 <-> 10 <-> 7 -> NULL

key = 10

Output

NULL <- 4 <-> 6 <-> 7 -> NULL


===============================================================================
Golden Observation
===============================================================================

Deleting ONE node in a Doubly Linked List is already easy because
every node knows both of its neighbours.

Whenever we find the key,

we simply remove that node by connecting

        previous node

                directly to

        next node.

So the whole problem becomes

        Traverse

                ↓

        Found key?

                ↓

        Delete node

                ↓

        Continue traversal

Nothing more.

===============================================================================
Quick Algorithm (30 Seconds)
===============================================================================

current = head

while current

    if current.data == key

        save prev
        save next

        connect prev <-> next

        move current to next

    else

        move current forward

return head

===============================================================================
Quick Pseudo Code
===============================================================================

current = head

while current

    if current.data == key

        if current is head

            head = head.next

        prev = current.prev
        next = current.next

        if prev

            prev.next = next

        if next

            next.prev = prev

        current = next

    else

        current = current.next

return head

===============================================================================
Approach
===============================================================================

Traverse the Doubly Linked List.

Whenever we encounter the key,

disconnect that node from the list.

To disconnect,

we connect

        previous node

directly with

        next node.

Then continue traversal.

Since every node is visited only once,

Time Complexity = O(n)

Space Complexity = O(1)

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
    # Delete All Occurrences
    # -------------------------------------------------------------------------

    def delete_all_occurrences(self, key):

        current = self.head

        while current:

            # --------------------------------------------------------------
            # Key found
            # --------------------------------------------------------------

            if current.data == key:

                # Save neighbours BEFORE disconnecting

                prev_node = current.prev
                next_node = current.next

                # ----------------------------------------------------------
                # Special Case
                # Deleting Head
                # ----------------------------------------------------------

                if current == self.head:

                    self.head = next_node

                # ----------------------------------------------------------
                # Connect previous node to next node
                # ----------------------------------------------------------

                if prev_node:

                    prev_node.next = next_node

                # ----------------------------------------------------------
                # Connect next node back to previous node
                # ----------------------------------------------------------

                if next_node:

                    next_node.prev = prev_node

                # ----------------------------------------------------------
                # Continue traversal
                #
                # DO NOT use current.next because current
                # has already been disconnected.
                # ----------------------------------------------------------

                current = next_node

            else:

                current = current.next


# =============================================================================
# Driver Code
# =============================================================================

if __name__ == "__main__":

    dll = DoublyLinkedList()

    values = [4, 10, 6, 10, 7, 10]

    for value in values:
        dll.insert_tail(value)

    print("Original DLL")
    dll.traverse()

    dll.delete_all_occurrences(10)

    print("\nAfter deleting all 10's")
    dll.traverse()


"""
===============================================================================
Dry Run
===============================================================================

Initial

4 <-> 10 <-> 6 <-> 10 <-> 7

current = 4

Not key

Move


--------------------------------

current = 10

prev = 4

next = 6


Reconnect


4 <---------> 6

Delete 10

Move to 6


--------------------------------

current = 6

Not key

Move


--------------------------------

current = 10

prev = 6

next = 7

Reconnect


6 <---------> 7

Delete

Move to 7


--------------------------------

Finished

4 <-> 6 <-> 7

===============================================================================
Mental Checklist
===============================================================================

✓ Save prev node

✓ Save next node

✓ Connect prev -> next

✓ Connect next -> prev

✓ Move to next node

===============================================================================
Common Mistakes
===============================================================================

❌ Forgetting to update head

If the first node is deleted,

head must change.

--------------------------------

❌ Writing

current = current.next

AFTER deleting current.

Wrong.

Save next first.

Then move.

--------------------------------

❌ Forgetting

next.prev = prev

DLL requires BOTH directions.

Updating only one pointer breaks the list.

===============================================================================
Delete Node Pattern
===============================================================================

Whenever deleting a node from a DLL

Always remember these four steps

Step 1

Save neighbours

        prev
        next

↓

Step 2

prev.next = next

↓

Step 3

next.prev = prev

↓

Step 4

Move to next node

This tiny pattern is reused in

✓ Delete Node

✓ Delete Duplicates

✓ Delete All Occurrences

✓ LRU Cache

✓ Browser History

✓ Text Editor

===============================================================================
Time Complexity
===============================================================================

O(n)

Every node is visited once.

===============================================================================
Space Complexity
===============================================================================

O(1)

===============================================================================
Takeaway
===============================================================================

This problem is NOT really about deleting values.

It is about mastering the universal

        "Delete Node in DLL"

pattern.

Whenever you remove a node from a Doubly Linked List,

think only one thing:

        Save neighbours

                ↓

        Connect neighbours

                ↓

        Continue traversal

Everything else naturally follows.

===============================================================================
"""