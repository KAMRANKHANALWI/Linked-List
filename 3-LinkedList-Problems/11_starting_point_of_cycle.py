"""
===============================================================================
                    STARTING POINT OF CYCLE IN LINKED LIST
===============================================================================

Problem Statement
-----------------
Given the head of a singly linked list, return the node where the cycle begins.

If there is no cycle, return None.

Example

1 -> 2 -> 3 -> 4 -> 5
          ↑         ↓
          └─────────┘

Output

Node with value 3

-------------------------------------------------------------------------------
Pattern Learned ⭐⭐⭐
-------------------------------------------------------------------------------

Slow & Fast Pointer (Floyd's Cycle Detection Algorithm)

-------------------------------------------------------------------------------
Intuition
-------------------------------------------------------------------------------

Approach 1 (Brute Force)

Store every visited node in a HashSet.

The first node visited twice is the starting point of the cycle.

---------------------------------------------------------

Approach 2 (Optimal)

Step 1

Use Floyd's Algorithm to detect the cycle.

Step 2

Once Slow and Fast meet,

move one pointer back to the head.

Now move both pointers one step at a time.

The node where they meet again is the starting point of the cycle.

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

    def cycle_start_brute(self, head):
        """
        Store every visited node.

        The first repeated node is the
        starting point of the cycle.
        """

        visited = set()

        temp = head

        while temp:

            if temp in visited:
                return temp

            visited.add(temp)
            temp = temp.next

        return None

    # ------------------------------------------------------------------------
    # Optimal
    # ------------------------------------------------------------------------

    def cycle_start(self, head):
        """
        Floyd's Cycle Detection Algorithm.
        """

        slow = head
        fast = head

        # Detect the cycle
        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:

                # Move one pointer to head
                slow = head

                # Move both one step
                while slow != fast:

                    slow = slow.next
                    fast = fast.next

                return slow

        return None


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

    start = solution.cycle_start(ll.head)

    if start:
        print("Cycle Starts At :", start.data)
    else:
        print("No Cycle")


"""
===============================================================================
Dry Run (Optimal)

1 -> 2 -> 3 -> 4 -> 5
          ↑         ↓
          └─────────┘

Step 1

Slow and Fast meet somewhere inside the cycle.

(Not necessarily at the starting node.)

---------------------------------------------------------

Step 2

Move Slow back to the head.

Head

Slow

↓

1 -> 2 -> 3 -> 4 -> 5
          ↑         ↓
          └─────────┘

Fast stays at the meeting point.

---------------------------------------------------------

Step 3

Move both pointers one step at a time.

Eventually,

Slow == Fast

at Node 3.

Answer = Node 3

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

1. Detect the cycle.

2. Move one pointer back to the head.

3. Move both pointers one step at a time.

The node where they meet is the starting point of the cycle.

===============================================================================
"""