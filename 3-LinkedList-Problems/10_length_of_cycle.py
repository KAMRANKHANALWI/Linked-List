"""
===============================================================================
                    LENGTH OF CYCLE IN LINKED LIST
===============================================================================

Problem Statement
-----------------
Given the head of a singly linked list, return the length of the cycle.

If there is no cycle, return 0.

Example

1 -> 2 -> 3 -> 4 -> 5
          ↑         ↓
          └─────────┘

Output

3

-------------------------------------------------------------------------------
Pattern Learned ⭐⭐⭐
-------------------------------------------------------------------------------

Slow & Fast Pointer (Floyd's Cycle Detection Algorithm)

-------------------------------------------------------------------------------
Intuition
-------------------------------------------------------------------------------

Approach 1 (Brute Force)

Store every visited node in a HashMap.

When a node is visited again,

Current Step - First Visited Step

gives the cycle length.

---------------------------------------------------------

Approach 2 (Optimal)

First detect the cycle using Floyd's Algorithm.

Once Slow and Fast meet,

keep one pointer fixed.

Move the other pointer until it reaches the same node again.

The number of steps taken is the length of the cycle.

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


# ============================================================================
# Solution
# ============================================================================

class Solution:

    # ------------------------------------------------------------------------
    # Brute Force
    # ------------------------------------------------------------------------

    def cycle_length_brute(self, head):
        """
        Store the first occurrence of every node.

        When a node repeats,

        Current Step - First Step = Cycle Length
        """

        visited = {}

        step = 0
        temp = head

        while temp:

            if temp in visited:
                return step - visited[temp]

            visited[temp] = step

            step += 1
            temp = temp.next

        return 0

    # ------------------------------------------------------------------------
    # Optimal
    # ------------------------------------------------------------------------

    def cycle_length(self, head):
        """
        Detect the cycle first.

        Then count the nodes inside the cycle.
        """

        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:

                length = 1
                current = slow.next

                while current != slow:

                    length += 1
                    current = current.next

                return length

        return 0


# ============================================================================
# Driver Code
# ============================================================================

if __name__ == "__main__":

    ll = LinkedList()

    for value in [1, 2, 3, 4, 5]:
        ll.insert_tail(value)

    # Create cycle
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

    print("Cycle Length :", solution.cycle_length(ll.head))


"""
===============================================================================
Dry Run (Optimal)

1 -> 2 -> 3 -> 4 -> 5
          ↑         ↓
          └─────────┘

Step 1

Detect the cycle.

Slow == Fast

↓

Meeting Point

Step 2

Keep Slow fixed.

Move another pointer around the cycle.

4 → 5 → 3 → 4

Steps

1

2

3

Reached the same node.

Cycle Length = 3

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

Detect the cycle first.

Once the pointers meet,

traverse one complete loop.

The number of nodes visited is the cycle length.

This idea is reused in the next problem:

• Starting Point of Cycle

===============================================================================
"""