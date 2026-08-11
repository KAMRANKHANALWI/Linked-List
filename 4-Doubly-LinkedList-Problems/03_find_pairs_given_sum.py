"""
====================================================================================
PROBLEM: Find Pairs With Given Sum in a Sorted Doubly Linked List
====================================================================================

Problem Statement
-----------------
Given the head of a **sorted Doubly Linked List** and a target value.

Return every pair of nodes whose sum equals the target.

Example

DLL:
1 <-> 2 <-> 3 <-> 4 <-> 9

Target = 5

Output:
[(1,4), (2,3)]


====================================================================================
PATTERN
====================================================================================

✔ Two Pointers
✔ Sorted Data Structure
✔ Doubly Linked List

This is the Linked List version of:

Two Sum II (Sorted Array)

The only difference is that instead of array indices, we move
using next and prev pointers.


====================================================================================
QUICK INTERVIEW PSEUDO CODE
====================================================================================

findTail(head)

left = head
right = tail

answer = []

while left != right
      and left.prev != right:

    current = left.data + right.data

    if current == target

        add pair

        left = left.next
        right = right.prev

    elif current < target

        left = left.next

    else

        right = right.prev

return answer


====================================================================================
GOLDEN OBSERVATION
====================================================================================

The list is SORTED.

That single word changes everything.

Instead of checking every pair,

we can place

Left Pointer  -> smallest value
Right Pointer -> largest value

Exactly like Two Sum on sorted arrays.


Example

1 <-> 2 <-> 3 <-> 4 <-> 9

L                 R

Current Sum

1+9 = 10

Too large.

Since list is sorted,

moving LEFT forward would increase the sum.

That is the opposite of what we want.

So move RIGHT backward.


Now

1+4 = 5

Found.


Store answer.

Move BOTH pointers.


====================================================================================
WHY MOVE BOTH AFTER FINDING A PAIR?
====================================================================================

Suppose

1 2 3 4 9

Target = 5

Found

1 + 4

Could

1

form another valid pair?

No.

Could

4

form another valid pair?

No.

Because the list is sorted.

Therefore we safely move BOTH pointers.


====================================================================================
DECISION TABLE
====================================================================================

Current Sum == Target

Store pair

Move Left
Move Right


-----------------------------------------

Current Sum < Target

Need a larger sum.

Move Left.


-----------------------------------------

Current Sum > Target

Need a smaller sum.

Move Right.


====================================================================================
WHY DOES MOVING LEFT INCREASE THE SUM?
====================================================================================

Sorted DLL

1 <-> 2 <-> 3 <-> 4 <-> 9

Left always moves toward larger values.

Right always moves toward smaller values.

Therefore

Move Left
=========
Sum increases.

Move Right
==========
Sum decreases.


====================================================================================
STOPPING CONDITION
====================================================================================

We stop when

left == right

or

left.prev == right

because the pointers have crossed.

Every possible pair has already been checked.


====================================================================================
APPROACH 1 — Brute Force
====================================================================================

For every node

compare it with every node after it.

Time Complexity

O(N²)

Space

O(1)


Pseudo Code

for every node i

    for every node after i

        if sum == target

            store pair


====================================================================================
APPROACH 2 — Optimal (Two Pointers)
====================================================================================

STEP 1

Find Tail.

STEP 2

Left = Head

Right = Tail

STEP 3

While pointers haven't crossed

Compute current sum.

Move pointers according to comparison.

Store valid pairs.


Time Complexity

Finding Tail

O(N)

Traversal

O(N)

Total

O(N)

Space

O(1)
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


# =============================================================================
# Doubly Linked List Node
# =============================================================================

@dataclass
class Node:
    data: int
    prev: Optional["Node"] = None
    next: Optional["Node"] = None


# =============================================================================
# Utility Functions
# =============================================================================

def build_dll(values):
    """
    Build a Doubly Linked List.

    Example

    Input

    [1,2,3,4]

    Output

    1 <-> 2 <-> 3 <-> 4
    """

    if not values:
        return None

    head = Node(values[0])
    current = head

    for value in values[1:]:

        new_node = Node(value)

        current.next = new_node
        new_node.prev = current

        current = new_node

    return head


def print_dll(head):
    """Print the Doubly Linked List."""

    current = head

    while current:

        print(current.data, end=" <-> " if current.next else "")

        current = current.next

    print()


# =============================================================================
# Helper Function
# =============================================================================

def find_tail(head: Optional[Node]) -> Optional[Node]:
    """
    Return the last node of the DLL.

    Example

    1 <-> 2 <-> 3 <-> 4

                     ↑
                  return
    """

    if head is None:
        return None

    current = head

    while current.next:
        current = current.next

    return current


# =============================================================================
# Optimal Solution
# =============================================================================

def find_pairs_with_sum(head: Optional[Node], target: int):
    """
    Return every pair whose sum equals target.

    Time Complexity
    ----------------
    O(N)

    Space Complexity
    -----------------
    O(1)
    """

    pairs = []

    if head is None:
        return pairs

    left = head
    right = find_tail(head)

    # ---------------------------------------------------------
    # Continue until pointers meet or cross.
    # ---------------------------------------------------------

    while (
        left is not None
        and right is not None
        and left != right
        and left.prev != right
    ):

        current_sum = left.data + right.data

        # -----------------------------------------------------
        # Perfect pair found.
        # -----------------------------------------------------

        if current_sum == target:

            pairs.append((left.data, right.data))

            left = left.next
            right = right.prev

        # -----------------------------------------------------
        # Need a larger sum.
        # -----------------------------------------------------

        elif current_sum < target:

            left = left.next

        # -----------------------------------------------------
        # Need a smaller sum.
        # -----------------------------------------------------

        else:

            right = right.prev

    return pairs


# =============================================================================
# Dry Run
# =============================================================================

head = build_dll([1, 2, 3, 4, 9])

print("Original DLL:")
print_dll(head)

pairs = find_pairs_with_sum(head, 5)

print("\nPairs with sum = 5")
print(pairs)


"""
Expected Output

Original DLL

1 <-> 2 <-> 3 <-> 4 <-> 9

Pairs

[(1,4), (2,3)]


====================================================================================
INTERVIEW RECAP
====================================================================================

Q1. Why does this work?

Because the DLL is sorted.

------------------------------------------------------------

Q2. Why move Left when sum is small?

Moving Left increases the sum.

------------------------------------------------------------

Q3. Why move Right when sum is large?

Moving Right decreases the sum.

------------------------------------------------------------

Q4. Why move BOTH after finding a pair?

Neither value can participate in another valid pair.

------------------------------------------------------------

Q5. Time Complexity

Find Tail

O(N)

Traversal

O(N)

Total

O(N)

------------------------------------------------------------

Q6. Space Complexity

O(1)

(excluding output list)


====================================================================================
KEY TAKEAWAY
====================================================================================

Whenever you see

✔ Sorted Array

or

✔ Sorted Doubly Linked List

Immediately think

TWO POINTERS.

This pattern appears repeatedly in interviews.
"""