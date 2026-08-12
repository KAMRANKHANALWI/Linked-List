"""
===============================================================================
                     FLATTEN A LINKED LIST
===============================================================================

Problem Statement
-----------------
You are given a special linked list.

Each node contains two pointers:

1. next  -> points to the next linked list
2. child -> points to a sorted linked list

Flatten the entire structure into ONE sorted linked list.

The final linked list should use ONLY the child pointers.

Example

                next
      3 ----------------> 2 ----------------> 1 ----------------> 4 ----------------> 5
      |                  |                  |                  |                  |
      |                  |                  |                  |                  |
      v                  v                  v                  v                  v
     NULL               10                  7                  9                  6
                                            |                                     |
                                            v                                     v
                                           11                                     8
                                            |
                                            v
                                           12


Expected Output

1
↓
2
↓
3
↓
4
↓
5
↓
6
↓
7
↓
8
↓
9
↓
10
↓
11
↓
12


===============================================================================
PATTERN
===============================================================================

✔ Merge Two Sorted Lists
✔ Recursion
✔ Divide and Conquer

This problem is basically

Merge Two Sorted Lists

+

Recursion

===============================================================================
OBSERVATION
===============================================================================

Look carefully.

Each vertical linked list is ALREADY SORTED.

Example

3

-------------------------

2
|
10

-------------------------

1
|
7
|
11
|
12

-------------------------

4
|
9

-------------------------

5
|
6
|
8


So this problem is NOT asking us to sort each list.

Instead,

it is asking us to MERGE multiple sorted linked lists.

That should immediately remind us of

Merge Two Sorted Lists.

===============================================================================
APPROACH 1 : Brute Force
===============================================================================

Idea

Instead of worrying about pointers,

collect every value,

sort them,

then build a brand new linked list.

Visualization

Input

3
2
10
1
7
11
12
4
9
5
6
8

↓

Store into an array

[3,2,10,1,7,11,12,4,9,5,6,8]

↓

Sort

[1,2,3,4,5,6,7,8,9,10,11,12]

↓

Build a new linked list

1
↓
2
↓
3
↓
4
↓
5
↓
6
↓
7
↓
8
↓
9
↓
10
↓
11
↓
12


Pseudo Code

Create empty array

Traverse every linked list

Store all values

Sort the array

Create a new linked list

Return head


Time Complexity

Collect Values

O(N)

Sorting

O(N log N)

Building New List

O(N)

Overall

O(N log N)


Space Complexity

O(N)

Extra array
Extra linked list

===============================================================================
CAN WE DO BETTER?
===============================================================================

Yes.

Notice,

every vertical list is already sorted.

Instead of

Collect

↓

Sort

↓

Build

we can simply

Merge

↓

Merge

↓

Merge

Exactly like Merge Two Sorted Lists.

The only question is

How do we merge FIVE sorted linked lists?

===============================================================================
GOLDEN OBSERVATION
===============================================================================

Suppose we have

3 ----> 2 ----> 1 ----> 4 ----> 5

Should we merge

3

with

2

first?

No.

Because after that

we still have

Merged(3,2)

+

1

+

4

+

5


Instead,

let the remaining linked lists flatten themselves first.

Then merge the current linked list into that answer.

This naturally leads to recursion.

===============================================================================
CORE RECURSION
===============================================================================

merged_head = flatten(head.next)

return merge(head, merged_head)

Read this like English.

Current List says

------------------------------------------------------------

"Dear remaining linked lists,

Please flatten yourselves first.

Once you become ONE sorted linked list,

I'll merge myself into you."

------------------------------------------------------------

That's literally the whole recursion.

===============================================================================
RECURSION VISUALIZATION
===============================================================================

Instead of imagining recursion as something magical,

imagine every function is simply WAITING.

CALLS

flatten(3)

        waits for

            flatten(2)

                    waits for

                        flatten(1)

                                waits for

                                    flatten(4)

                                            waits for

                                                flatten(5)

                                                        |

                                                        |

                                                  Base Case

                                                  return 5


Nothing has been merged yet.

Every function is simply waiting.


===============================================================================
NOW THE RETURNS START
===============================================================================

flatten(5)

returns

5

↑


flatten(4)

merged_head = 5

return merge(4,5)

↓

returns

4
|
5
|
6
|
8
|
9


↑


flatten(1)

merged_head =

4
|
5
|
6
|
8
|
9


return merge(1, merged_head)

↓

returns

1
|
4
|
5
|
6
|
7
|
8
|
9
|
11
|
12


↑


flatten(2)

merged_head =

1
|
4
|
5
|
6
|
7
|
8
|
9
|
11
|
12


return merge(2, merged_head)

↓

returns

1
|
2
|
4
|
5
|
6
|
7
|
8
|
9
|
10
|
11
|
12


↑


flatten(3)

merged_head =

1
|
2
|
4
|
5
|
6
|
7
|
8
|
9
|
10
|
11
|
12


return merge(3, merged_head)

↓

FINAL ANSWER

1
↓
2
↓
3
↓
4
↓
5
↓
6
↓
7
↓
8
↓
9
↓
10
↓
11
↓
12


===============================================================================
MENTAL MODEL
===============================================================================

Don't think

"Recursion calls Recursion."

Think

Current List

↓

Wait

↓

Remaining Lists Finish

↓

Merge Yourself

↓

Return


Or even shorter

Flatten Right

↓

Merge Current

↓

Return

===============================================================================
"""

# =============================================================================
# Node Definition
# =============================================================================


class Node:
    """
    Represents one node of the special linked list.

    Each node has

    next  -> next linked list

    child -> next node inside the same linked list
    """

    def __init__(self, data):
        self.data = data
        self.next = None
        self.child = None


# =============================================================================
# Helper Functions (For Learning)
# =============================================================================


def print_child_list(head):
    """
    Prints a child linked list.

    Example

    1
    |
    2
    |
    3

    Output

    1 -> 2 -> 3
    """

    temp = head

    while temp:

        print(temp.data, end=" -> " if temp.child else "")

        temp = temp.child

    print()


# =============================================================================
# Approach 1 : Brute Force
# =============================================================================

"""
Idea

Visit every node.

Store every value.

Sort them.

Build a brand new linked list.

Although this isn't the expected interview solution,
it helps us understand the problem first.

Pseudo Code

values = []

Traverse every vertical linked list

Store values

Sort values

Create new linked list

Return head
"""


class BruteForceSolution:

    # -------------------------------------------------------------------------
    # Store every value
    # -------------------------------------------------------------------------

    def _collect_values(self, head, values):
        """
        Traverse every linked list.

        Example

        3 -> 2 -> 1

        becomes

        [3,2,10,1,7,11,12...]
        """

        horizontal = head

        while horizontal:

            vertical = horizontal

            while vertical:

                values.append(vertical.data)

                vertical = vertical.child

            horizontal = horizontal.next

    # -------------------------------------------------------------------------
    # Build a new child linked list
    # -------------------------------------------------------------------------

    def _build_child_list(self, values):
        """
        Build

        1
        |
        2
        |
        3
        """

        if not values:
            return None

        head = Node(values[0])

        current = head

        for value in values[1:]:

            current.child = Node(value)

            current = current.child

        return head

    # -------------------------------------------------------------------------
    # Main Function
    # -------------------------------------------------------------------------

    def flatten(self, head):
        """
        Brute Force Solution

        Time

        O(N log N)

        Space

        O(N)
        """

        if head is None:
            return None

        values = []

        # Step 1
        # Collect every value

        self._collect_values(head, values)

        # Step 2
        # Sort values

        values.sort()

        # Step 3
        # Build new child linked list

        return self._build_child_list(values)


# =============================================================================
# Dry Run (Brute Force)
# =============================================================================

"""
Input

3
2
10
1
7
11
12
4
9
5
6
8

--------------------------------------

Collect

↓

[3,2,10,1,7,11,12,4,9,5,6,8]

--------------------------------------

Sort

↓

[1,2,3,4,5,6,7,8,9,10,11,12]

--------------------------------------

Create

1
|
2
|
3
|
4
|
5
|
6
|
7
|
8
|
9
|
10
|
11
|
12

Done.

--------------------------------------

Time

O(N log N)

Space

O(N)
"""

# =============================================================================
# Why We Need a Better Solution
# =============================================================================

"""
Notice something...

Every vertical linked list was already sorted.

So why

Collect

↓

Sort

↓

Rebuild

when we already have

Sorted List

+

Sorted List

+

Sorted List

+

Sorted List

?

Instead,

reuse the idea from

Merge Two Sorted Lists.

That gives us an O(N) merge operation.

Now the only question becomes

How do we merge ALL the linked lists?

That's exactly where recursion helps.
"""

# =============================================================================
# Helper Function : Merge Two Sorted Child Linked Lists
# =============================================================================

"""
This is exactly the same problem as

Merge Two Sorted Linked Lists.

The only difference is

Instead of using

next

we use

child.

Example

List 1

1
|
7
|
11

-------------------------

List 2

4
|
9

-------------------------

Merged

1
|
4
|
7
|
9
|
11

"""


def merge(list1, list2):
    """
    Merge two sorted child linked lists.

    Returns the head of the merged list.

    Time  : O(n1 + n2)
    Space : O(1)
    """

    # Dummy node simplifies merging
    dummy = Node(-1)

    current = dummy

    # ---------------------------------------------------------
    # Pick the smaller node every time.
    # ---------------------------------------------------------

    while list1 and list2:

        if list1.data <= list2.data:

            current.child = list1

            list1 = list1.child

        else:

            current.child = list2

            list2 = list2.child

        # Move current forward
        current = current.child

        # The flattened list should only use child pointers.
        current.next = None

    # ---------------------------------------------------------
    # Attach the remaining list.
    # ---------------------------------------------------------

    if list1:
        current.child = list1

    else:
        current.child = list2

    return dummy.child


# =============================================================================
# Approach 2 : Optimal (Recursion + Merge)
# =============================================================================

"""
Golden Observation

Don't flatten everything at once.

Instead,

flatten everything on the RIGHT first.

Then merge the current linked list into that answer.

Instead of

merge(3,2)

↓

merge(result,1)

↓

merge(result,4)

↓

merge(result,5)

we do

merge(4,5)

↓

merge(1, result)

↓

merge(2, result)

↓

merge(3, result)

Much cleaner.

===============================================================================
Pseudo Code
===============================================================================

flatten(head)

    if only one list remains

        return head

    merged_head = flatten(head.next)

    return merge(head, merged_head)

"""


class OptimalSolution:

    def flatten(self, head):
        """
        Flatten the linked list using recursion.

        Time  : O(N * K)
                (N = total nodes, K = number of linked lists.
                 A node can be re-merged once per remaining
                 list, so cost is not linear — see the full
                 breakdown in the "Complexity Analysis" section.)

        Space : O(number of linked lists)
                due to recursion.
        """

        # -----------------------------------------------------
        # Base Case
        # -----------------------------------------------------

        if head is None or head.next is None:
            return head

        # -----------------------------------------------------
        # First flatten everything on the right.
        # -----------------------------------------------------

        merged_head = self.flatten(head.next)

        # -----------------------------------------------------
        # Merge current list with already flattened list.
        # -----------------------------------------------------

        return merge(head, merged_head)


# =============================================================================
# Dry Run (Optimal)
# =============================================================================

"""
Suppose we have

3 ----> 2 ----> 1 ----> 4 ----> 5

CALLS
-------------------------------------------------------

flatten(3)

↓

flatten(2)

↓

flatten(1)

↓

flatten(4)

↓

flatten(5)

↓

Base Case

return 5

-------------------------------------------------------
RETURNS
-------------------------------------------------------

flatten(4)

merged_head = 5

↓

merge(4,5)

↓

returns

4
|
5
|
6
|
8
|
9

-------------------------------------------------------

flatten(1)

merged_head

4
|
5
|
6
|
8
|
9

↓

merge(1, merged_head)

↓

returns

1
|
4
|
5
|
6
|
7
|
8
|
9
|
11
|
12

-------------------------------------------------------

flatten(2)

↓

merge(2, previous)

↓

returns

1
|
2
|
4
|
5
|
6
|
7
|
8
|
9
|
10
|
11
|
12

-------------------------------------------------------

flatten(3)

↓

merge(3, previous)

↓

Final Answer

1
|
2
|
3
|
4
|
5
|
6
|
7
|
8
|
9
|
10
|
11
|
12

"""

# =============================================================================
# Example Usage (For Learning)
# =============================================================================

"""
Example

                next
      3 ----------------> 2 ----------------> 1 ----------------> 4 ----------------> 5
      |                  |                  |                  |                  |
      |                  |                  |                  |                  |
      v                  v                  v                  v                  v
     NULL               10                  7                  9                  6
                                            |                                     |
                                            v                                     v
                                           11                                     8
                                            |
                                            v
                                           12

After Flattening

1
|
2
|
3
|
4
|
5
|
6
|
7
|
8
|
9
|
10
|
11
|
12

(All connected using child pointers.)
"""

# Driver code intentionally omitted because constructing this
# special linked list manually is lengthy and platform-specific.
#
# On coding platforms (LeetCode / GFG),
# the linked list is already created for you.
#
# You only need to implement flatten().


# =============================================================================
# Complexity Analysis
# =============================================================================

"""
------------------------------------------------------------
Brute Force
------------------------------------------------------------

Collect Values

O(N)

Sort

O(N log N)

Build New List

O(N)

Overall

O(N log N)

Space

O(N)

------------------------------------------------------------
Optimal Recursive Merge
------------------------------------------------------------

Suppose

k = number of linked lists

n = total number of nodes

Every recursive call merges

Current List

with

Already Flattened Lists

Worst Case

O(n × k)

Extra Space

O(k)

(recursion stack)

------------------------------------------------------------
Can We Do Even Better?
------------------------------------------------------------

YES.

Exactly like

Merge K Sorted Lists

we can use

Min Heap (Priority Queue)

Time

O(n log k)

But that solution is beyond the scope of this
Striver Linked List sheet.

The recursive merge solution is the expected interview approach.
"""


# =============================================================================
# Pattern Recognition
# =============================================================================

"""
Whenever you see

✔ Multiple Sorted Linked Lists

Immediately think

Merge Two Sorted Lists

Then ask yourself

How do I merge ALL of them?

Possible approaches

1.

Merge one by one

↓

Recursion

(This problem)

------------------------------------

2.

Merge pairwise

↓

Merge K Sorted Lists

------------------------------------

3.

Min Heap

↓

O(n log k)

(Most Optimal General Solution)
"""


# =============================================================================
# Interview Takeaways
# =============================================================================

"""
This problem is NOT about recursion.

It is about recognizing that

Flatten

=

Repeated Merge Two Sorted Lists.

------------------------------------------------------------

The recursion simply decides

the ORDER of merging.

Instead of

Merge Left → Right

it naturally performs

Merge Right → Left

while returning.

------------------------------------------------------------

Always remember this picture

CALLS

flatten(3)

↓

flatten(2)

↓

flatten(1)

↓

flatten(4)

↓

flatten(5)

↓

return

----------------------------------------

RETURNS

merge(4,5)

↓

merge(1, merged)

↓

merge(2, merged)

↓

merge(3, merged)

↓

FINAL ANSWER

----------------------------------------

Mental Model

Flatten Right

↓

Merge Current

↓

Return

That's the entire algorithm.

If you remember these three steps,

you can reconstruct the code anytime.
"""


# =============================================================================
# Key Pattern Learned
# =============================================================================

"""
Pattern Added to Repository

✔ Merge Two Sorted Lists
✔ Recursion (Post-order Style)
✔ Divide and Conquer

This is one of the cleanest examples of

"Do all work while recursion RETURNS."

Instead of

doing work while going down,

we do

all the merging while coming back.

That's why the recursion feels like

a loop running backwards.
"""
