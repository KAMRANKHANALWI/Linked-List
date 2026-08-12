"""
============================================================
Problem: Reverse Nodes in K Group
============================================================

Problem Statement
-----------------
Given the head of a linked list, reverse every group of K nodes.

If the remaining nodes are fewer than K,
leave them exactly as they are.

Example

Input

1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10

K = 3

Output

3 → 2 → 1 → 6 → 5 → 4 → 9 → 8 → 7 → 10

------------------------------------------------------------
Golden Observation
------------------------------------------------------------

Instead of trying to reverse the whole list at once,

Think of the list as many small linked lists.

Example

1 → 2 → 3 | 4 → 5 → 6 | 7 → 8 → 9 | 10

Reverse each small list independently.

Then reconnect them.

So every iteration performs the same cycle:

1. Find kth node
2. Save next group's starting node
3. Disconnect current group
4. Reverse current group
5. Connect previous group
6. Move forward

------------------------------------------------------------
Pseudo Code
------------------------------------------------------------

temp = head
previous_group_tail = None

while temp exists

    kth_node = find kth node from temp

    if kth node doesn't exist

        connect previous group with remaining nodes
        break

    next_group = kth_node.next

    cut current group

    reverse current group

    if first group
        update head
    else
        connect previous group

    previous_group_tail = current group's tail
    temp = next_group

return head
"""

# ==========================================================
# Node Definition
# ==========================================================


class Node:
    """
    Doubly unnecessary for this problem.
    Standard Singly Linked List Node.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


# ==========================================================
# Helper Function 1
# Reverse a complete linked list
# ==========================================================


def reverse_linked_list(head):
    """
    Reverses an entire linked list.

    Example

    1 → 2 → 3

    becomes

    3 → 2 → 1
    """

    previous = None
    current = head

    while current:

        next_node = current.next

        current.next = previous

        previous = current

        current = next_node

    return previous


# ==========================================================
# Helper Function 2
# Find kth node from current node
# ==========================================================


def get_kth_node(temp, k):
    """
    Returns the kth node starting from temp.

    Example

    temp

      ↓

    4 → 5 → 6 → 7

    K = 3

    returns node containing 6

    If K nodes don't exist,
    returns None.
    """

    k -= 1

    while temp and k > 0:
        temp = temp.next
        k -= 1

    return temp


# ==========================================================
# Main Function
# ==========================================================


def reverse_k_group(head, k):
    """
    Reverse every K nodes.

    Time  : O(N)
    Space : O(1)
    """

    if head is None or k == 1:
        return head

    # Beginning of current group
    temp = head

    # Tail of previously reversed group
    previous_group_tail = None

    while temp:

        # ---------------------------------------
        # Step 1
        # Find kth node
        # ---------------------------------------

        kth_node = get_kth_node(temp, k)

        # ---------------------------------------
        # If group size is smaller than K
        # leave it unchanged
        # ---------------------------------------

        if kth_node is None:

            if previous_group_tail:
                previous_group_tail.next = temp

            break

        # ---------------------------------------
        # Step 2
        # Save next group's starting node
        # ---------------------------------------

        next_group = kth_node.next

        # ---------------------------------------
        # Step 3
        # Disconnect current group
        # ---------------------------------------

        kth_node.next = None

        # ---------------------------------------
        # Step 4
        # Reverse current group
        # ---------------------------------------

        reverse_linked_list(temp)

        # ---------------------------------------
        # Step 5
        # Connect with previous group
        # ---------------------------------------

        if temp == head:

            # First reversal changes head
            head = kth_node

        else:

            previous_group_tail.next = kth_node

        # ---------------------------------------
        # Step 6
        # Update pointers for next iteration
        # ---------------------------------------

        previous_group_tail = temp

        temp = next_group

    return head


# ==========================================================
# Utility Functions
# ==========================================================


def build_linked_list(values):

    if not values:
        return None

    head = Node(values[0])
    current = head

    for value in values[1:]:
        current.next = Node(value)
        current = current.next

    return head


def print_linked_list(head):

    current = head

    while current:
        print(current.data, end=" -> " if current.next else "")
        current = current.next

    print()


# ==========================================================
# Driver Code
# ==========================================================

head = build_linked_list([1,2,3,4,5,6,7,8,9,10])

print("Original Linked List")
print_linked_list(head)

head = reverse_k_group(head, 3)

print("\nAfter Reversing Every 3 Nodes")
print_linked_list(head)

"""
Output

Original

1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10

After Reversing

3 -> 2 -> 1 -> 6 -> 5 -> 4 -> 9 -> 8 -> 7 -> 10
"""

# ==========================================================
# Complexity Analysis
# ==========================================================

"""
Time Complexity
---------------
Finding kth node across all groups : O(N)

Reversing all groups : O(N)

Overall

O(N)

--------------------------------------------

Space Complexity

O(1)

No extra data structures are used.

Only a few pointers are maintained.

--------------------------------------------

Key Interview Takeaways

✓ Think group by group.

✓ Always save the next group's starting node
  before disconnecting.

✓ Cut the group before reversing.

✓ First group updates the head.

✓ previous_group_tail connects consecutive groups.

✓ If fewer than K nodes remain,
  leave them unchanged.
"""