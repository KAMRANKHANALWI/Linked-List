"""
===============================================================================
                INTERSECTION OF TWO LINKED LISTS
===============================================================================

Problem Statement
-----------------
Given the heads of two singly linked lists, determine the node at which the
two linked lists intersect.

Return the intersecting node.

If the two linked lists do not intersect, return None.

IMPORTANT:
----------
Intersection is NOT based on node values.

It is based on the MEMORY ADDRESS of the node.

Example

List A

1 → 2 → 3
          \
           7 → 8 → 9
          /
List B

4 → 5

Answer

Node(7)

NOT because value = 7

Because both lists point to the EXACT SAME NODE.

===============================================================================
Observation
===============================================================================

Many beginners think

7 == 7

means intersection.

Wrong.

Consider

List A

1 → 7

List B

2 → 7

These are NOT intersecting if both 7s are different objects.

Correct comparison is

node1 is node2

NOT

node1.data == node2.data

===============================================================================
Approach 1 : Brute Force
===============================================================================

For every node in List A,

traverse the entire List B.

If any node address matches,

return that node.

Visualization

A1

compare with

B1 B2 B3 B4

A2

compare with

B1 B2 B3 B4

...

Eventually

common node found.

Time Complexity
---------------
O(N × M)

Space Complexity
----------------
O(1)

===============================================================================
Approach 2 : Better (HashSet)
===============================================================================

Store every node of List A inside a HashSet.

Then traverse List B.

If current node already exists in the set,

that's the intersection.

Visualization

List A

1 → 2 → 3 → 7 → 8

HashSet

{
1,
2,
3,
7,
8
}

Traverse B

4

Not Found

5

Not Found

7

Found

Return 7.

Time Complexity
---------------
O(N + M)

Space Complexity
----------------
O(N)

===============================================================================
Approach 3 : Optimal (Length Difference)
===============================================================================

Observation

Suppose

List A

1 → 2 → 3 → 7 → 8 → 9

Length = 6

List B

4 → 5 → 7 → 8 → 9

Length = 5

Difference = 1

The longer list has one extra node.

Move the longer list ahead by one node.

Now both pointers have equal distance to the end.

Move together.

Eventually they meet at the intersection.

Time Complexity
---------------
O(N + M)

Space Complexity
----------------
O(1)

===============================================================================
Approach 4 : Optimal (Pointer Switching)
===============================================================================

This is the most elegant solution.

Start

pointer1 = headA

pointer2 = headB

Move both together.

Whenever one pointer reaches NULL,

move it to the OTHER list's head.

Eventually

pointer1

travels

A + B

pointer2

travels

B + A

Both travel exactly the same total distance.

Therefore

they either

• meet at the intersection

or

• both become None.

No length calculation required.

Time Complexity
---------------
O(N + M)

Space Complexity
----------------
O(1)

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
# Better Solution (HashSet)
# =============================================================================


def intersection_hashset(head1, head2):

    visited = set()

    temp = head1

    while temp:

        visited.add(temp)
        temp = temp.next

    temp = head2

    while temp:

        if temp in visited:
            return temp

        temp = temp.next

    return None


# =============================================================================
# Helper Function
# =============================================================================


def get_length(head):

    length = 0

    while head:

        length += 1
        head = head.next

    return length


# =============================================================================
# Optimal Solution 1
# Length Difference
# =============================================================================


def intersection_length(head1, head2):

    len1 = get_length(head1)
    len2 = get_length(head2)

    ptr1 = head1
    ptr2 = head2

    # Move longer list ahead

    if len1 > len2:

        for _ in range(len1 - len2):
            ptr1 = ptr1.next

    else:

        for _ in range(len2 - len1):
            ptr2 = ptr2.next

    while ptr1 and ptr2:

        if ptr1 is ptr2:
            return ptr1

        ptr1 = ptr1.next
        ptr2 = ptr2.next

    return None


# =============================================================================
# Optimal Solution 2
# Pointer Switching (Striver's Favorite)
# =============================================================================


def intersection_pointer_switch(head1, head2):

    if head1 is None or head2 is None:
        return None

    ptr1 = head1
    ptr2 = head2

    while ptr1 is not ptr2:

        if ptr1:
            ptr1 = ptr1.next
        else:
            ptr1 = head2

        if ptr2:
            ptr2 = ptr2.next
        else:
            ptr2 = head1

    return ptr1


# =============================================================================
# Driver Code
# =============================================================================

if __name__ == "__main__":

    #
    # Shared Part
    #

    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)

    node7.next = node8
    node8.next = node9

    #
    # List A
    #

    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = node7

    #
    # List B
    #

    head2 = Node(4)
    head2.next = Node(5)
    head2.next.next = node7

    ans = intersection_hashset(head1, head2)
    print("HashSet :", ans.data if ans else None)

    ans = intersection_length(head1, head2)
    print("Length Difference :", ans.data if ans else None)

    ans = intersection_pointer_switch(head1, head2)
    print("Pointer Switching :", ans.data if ans else None)


"""
===============================================================================
Dry Run (Pointer Switching)

List A

1 → 2 → 3 → 7 → 8 → 9

List B

4 → 5 → 7 → 8 → 9

----------------------------------------------------

Pointer1

A

↓

B

Pointer2

B

↓

A

----------------------------------------------------

Total distance travelled

Pointer1

Length(A) + Length(B)

Pointer2

Length(B) + Length(A)

Equal.

Eventually both pointers enter the shared tail together.

Meeting Point = Intersection.

===============================================================================
Time Complexity

Brute Force

O(N × M)

HashSet

O(N + M)

Length Difference

O(N + M)

Pointer Switching

O(N + M)

===============================================================================
Space Complexity

Brute Force

O(1)

HashSet

O(N)

Length Difference

O(1)

Pointer Switching

O(1)

===============================================================================
Key Takeaways

1. Compare NODE REFERENCES, not node values.

2. HashSet is an excellent improvement over brute force.

3. Length Difference is a common interview technique.

4. Pointer Switching is one of the most elegant Linked List algorithms.

5. Whenever two linked lists have different lengths but share a common tail,
   think about either:

   • Aligning the lengths

   OR

   • Pointer Switching

===============================================================================
"""
