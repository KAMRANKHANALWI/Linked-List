"""
===============================================================================
                    LINKED LIST - BASIC OPERATIONS
===============================================================================

Goal:
    Implement all fundamental operations on a Singly Linked List.

Operations Covered:
    1. Traverse
    2. Length
    3. Search
    4. Insert at Head
    5. Insert at Tail
    6. Insert at Position
    7. Delete Head
    8. Delete Tail
    9. Delete at Position

Golden Pattern:
    temp = head
    while temp:
        # Work
        temp = temp.next

Time Complexity:
    Traverse            O(n)
    Length              O(n)
    Search              O(n)
    Insert Head         O(1)
    Insert Tail         O(n)
    Insert Position     O(n)
    Delete Head         O(1)
    Delete Tail         O(n)
    Delete Position     O(n)
===============================================================================
"""

# =============================================================================
# Node
# =============================================================================


class Node:
    """Represents one node of a Singly Linked List."""

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
    # Traverse
    # -------------------------------------------------------------------------

    def traverse(self):
        """Print all nodes."""

        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # -------------------------------------------------------------------------
    # Length
    # -------------------------------------------------------------------------

    def length(self):
        """Return number of nodes."""

        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        return count

    # -------------------------------------------------------------------------
    # Search
    # -------------------------------------------------------------------------

    def search(self, value):
        """Return True if value exists."""

        temp = self.head

        while temp:

            if temp.data == value:
                return True

            temp = temp.next

        return False

    # -------------------------------------------------------------------------
    # Insert at Head
    # -------------------------------------------------------------------------

    def insert_head(self, value):
        """Insert node at beginning."""

        new_node = Node(value)

        new_node.next = self.head
        self.head = new_node

    # -------------------------------------------------------------------------
    # Insert at Tail
    # -------------------------------------------------------------------------

    def insert_tail(self, value):
        """Insert node at end."""

        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node

    # -------------------------------------------------------------------------
    # Insert at Position (0-based)
    # -------------------------------------------------------------------------

    def insert_at_position(self, pos, value):

        if pos == 0:
            self.insert_head(value)
            return

        new_node = Node(value)

        temp = self.head

        for _ in range(pos - 1):
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

    # -------------------------------------------------------------------------
    # Delete Head
    # -------------------------------------------------------------------------

    def delete_head(self):

        if self.head:
            self.head = self.head.next

    # -------------------------------------------------------------------------
    # Delete Tail
    # -------------------------------------------------------------------------

    def delete_tail(self):

        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next.next:
            temp = temp.next

        temp.next = None

    # -------------------------------------------------------------------------
    # Delete at Position (0-based)
    # -------------------------------------------------------------------------

    def delete_at_position(self, pos):

        if pos == 0:
            self.delete_head()
            return

        temp = self.head

        for _ in range(pos - 1):
            temp = temp.next

        temp.next = temp.next.next


# =============================================================================
# Driver Code
# =============================================================================

if __name__ == "__main__":

    ll = LinkedList()

    ll.insert_head(20)
    ll.insert_head(10)

    ll.insert_tail(30)
    ll.insert_tail(40)
    ll.insert_tail(50)

    print("Traversal")
    ll.traverse()

    print("\nLength:", ll.length())

    print("Search 30 :", ll.search(30))
    print("Search 100:", ll.search(100))

    ll.insert_at_position(2, 25)

    print("\nAfter Insert at Position")
    ll.traverse()

    ll.delete_head()

    print("\nAfter Delete Head")
    ll.traverse()

    ll.delete_tail()

    print("\nAfter Delete Tail")
    ll.traverse()

    ll.delete_at_position(2)

    print("\nAfter Delete Position")
    ll.traverse()
