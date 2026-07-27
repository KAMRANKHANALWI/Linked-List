"""
===============================================================================
                        DETECT CYCLE IN LINKED LIST
===============================================================================

Problem Statement
-----------------
Given the head of a singly linked list, determine whether the linked list
contains a cycle.

Return True if a cycle exists, otherwise return False.

Example

1 -> 2 -> 3 -> 4 -> 5
          ↑         ↓
          └─────────┘

Output

True

-------------------------------------------------------------------------------
Pattern Learned ⭐⭐⭐
-------------------------------------------------------------------------------

Slow & Fast Pointer (Floyd's Cycle Detection Algorithm)

-------------------------------------------------------------------------------
Intuition
-------------------------------------------------------------------------------

Approach 1 (Brute Force)

Store every visited node in a HashSet.

If a node is visited again, a cycle exists.

---------------------------------------------------------

Approach 2 (Optimal)

Use two pointers.

• Slow moves one step.
• Fast moves two steps.

If a cycle exists,

Fast will eventually catch Slow.

If Fast reaches None,

the linked list has no cycle.

===============================================================================
"""


# ============================================================================
# Node
# ============================================================================

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# ============================================================================
# Linked List (Helper Class)
# ============================================================================

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_tail(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node

    def traverse(self, limit=15):
        """
        Print the linked list.

        'limit' avoids infinite printing if a cycle exists.
        """

        temp = self.head
        count = 0

        while temp and count < limit:

            print(temp.data, end=" -> ")

            temp = temp.next
            count += 1

        if temp:
            print("...")
        else:
            print("None")


# ============================================================================
# Solution
# ============================================================================

class Solution:

    # ------------------------------------------------------------------------
    # Brute Force
    # ------------------------------------------------------------------------

    def has_cycle_brute(self, head):
        """
        Store visited nodes inside a HashSet.
        """

        visited = set()

        temp = head

        while temp:

            if temp in visited:
                return True

            visited.add(temp)

            temp = temp.next

        return False

    # ------------------------------------------------------------------------
    # Optimal
    # ------------------------------------------------------------------------

    def has_cycle(self, head):
        """
        Floyd's Cycle Detection Algorithm.
        """

        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


# ============================================================================
# Driver Code
# ============================================================================

if __name__ == "__main__":

    ll = LinkedList()

    for value in [1, 2, 3, 4, 5]:
        ll.insert_tail(value)

    # Create a cycle:
    #
    # 1 -> 2 -> 3 -> 4 -> 5
    #           ↑         ↓
    #           └─────────┘

    third = ll.head.next.next
    tail = ll.head

    while tail.next:
        tail = tail.next

    tail.next = third

    solution = Solution()

    print("Cycle Exists :", solution.has_cycle(ll.head))


"""
===============================================================================
Dry Run (Optimal)

1 -> 2 -> 3 -> 4 -> 5
          ↑         ↓
          └─────────┘

Initially

Slow
Fast

↓

1

---------------------------------------------------------

Move

Slow

↓

2

Fast

↓

3

---------------------------------------------------------

Move

Slow

↓

3

Fast

↓

5

---------------------------------------------------------

Move

Slow

↓

4

Fast

↓

4

Slow == Fast

Cycle Detected.

===============================================================================

Complexity
===============================================================================

Brute Force

Time  : O(n)

Space : O(n)

---------------------------------------------------------

Optimal

Time  : O(n)

Space : O(1)

===============================================================================

Interview Takeaway
===============================================================================

Pattern : Slow & Fast Pointer ⭐⭐⭐

Slow moves one step.

Fast moves two steps.

If Fast ever meets Slow,

a cycle exists.

If Fast reaches None,

there is no cycle.

This same pattern is reused in:

• Length of Cycle
• Starting Point of Cycle
• Happy Number (Array/Math)

===============================================================================
"""