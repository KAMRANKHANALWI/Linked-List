"""
===============================================================================
                DOUBLY LINKED LIST - BASIC OPERATIONS
===============================================================================

Goal:
    Implement all fundamental operations on a Doubly Linked List.

Operations Covered:
    1. Forward Traversal
    2. Backward Traversal
    3. Length
    4. Search
    5. Insert at Head
    6. Insert at Tail
    7. Delete Head
    8. Delete Tail

Golden Rule:
    Every insertion/deletion must update BOTH next and prev pointers.

Time Complexity:
    Traverse            O(n)
    Length              O(n)
    Search              O(n)
    Insert Head         O(1)
    Insert Tail         O(n)
    Delete Head         O(1)
    Delete Tail         O(n)
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
    # Forward Traversal
    # -------------------------------------------------------------------------

    def traverse_forward(self):

        temp = self.head

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")

    # -------------------------------------------------------------------------
    # Backward Traversal
    # -------------------------------------------------------------------------

    def traverse_backward(self):

        if self.head is None:
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev

        print("None")

    # -------------------------------------------------------------------------
    # Length
    # -------------------------------------------------------------------------

    def length(self):

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

        new_node = Node(value)

        if self.head:
            self.head.prev = new_node
            new_node.next = self.head

        self.head = new_node

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
    # Delete Head
    # -------------------------------------------------------------------------

    def delete_head(self):

        if self.head is None:
            return

        self.head = self.head.next

        if self.head:
            self.head.prev = None

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

        while temp.next:
            temp = temp.next

        temp.prev.next = None


# =============================================================================
# Driver Code
# =============================================================================

if __name__ == "__main__":

    dll = DoublyLinkedList()

    dll.insert_head(20)
    dll.insert_head(10)

    dll.insert_tail(30)
    dll.insert_tail(40)
    dll.insert_tail(50)

    print("Forward Traversal")
    dll.traverse_forward()

    print("\nBackward Traversal")
    dll.traverse_backward()

    print("\nLength:", dll.length())

    print("Search 30 :", dll.search(30))
    print("Search 100:", dll.search(100))

    dll.delete_head()

    print("\nAfter Delete Head")
    dll.traverse_forward()

    dll.delete_tail()

    print("\nAfter Delete Tail")
    dll.traverse_forward()