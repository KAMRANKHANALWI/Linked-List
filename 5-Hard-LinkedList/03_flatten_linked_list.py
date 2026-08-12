"""
===============================================================================
                          FLATTEN A LINKED LIST
===============================================================================

Problem
-------
Each node has two pointers:
    next  -> the next linked list (horizontal)
    child -> a sorted linked list (vertical)

Flatten the whole structure into ONE sorted linked list, using
only `child` pointers.

                next
      3 --------> 2 --------> 1 --------> 4 --------> 5
      |           |           |           |           |
     NULL        10           7           9           6
                              |                        |
                              11                        8
                              |
                              12

Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11 -> 12

Pattern: Merge Two Sorted Lists + Recursion (postorder)

Golden Observation
-------------------
Every vertical list is already sorted -- so this isn't a sorting
problem, it's a MERGING problem: merge K sorted lists.

For merge order: don't merge 3 and 2 first. If you do, you're
still left holding merged(3,2) + 1 + 4 + 5. Instead, let the
REMAINING lists flatten themselves first, then merge the current
list into that result:

    merged_head = flatten(head.next)
    return merge(head, merged_head)

Read it like English: "Remaining lists, flatten yourselves first.
Once you're one sorted list, I'll merge myself into you."

That's the entire algorithm -- the recursion just decides the
merge ORDER (right-to-left instead of left-to-right):

    CALLS (going down, nothing merged yet)
    flatten(3) -> flatten(2) -> flatten(1) -> flatten(4) -> flatten(5)

    RETURNS (merging happens on the way back up)
    merge(4,5) -> merge(1,·) -> merge(2,·) -> merge(3,·) -> answer

Mental model: Flatten Right -> Merge Current -> Return.
"""


class Node:
    """next -> next list, child -> next node in the same list."""

    def __init__(self, data):
        self.data = data
        self.next = None
        self.child = None


def to_list(head):
    out = []
    while head:
        out.append(head.data)
        assert head.next is None, "next pointer wasn't cleared!"
        head = head.child
    return out


# =============================================================================
# Approach 1 : Brute Force -- ignore that each vertical list is sorted
# =============================================================================
"""
Idea: walk every node, dump every value into an array, sort it,
build a fresh list. Works, but throws away the fact that every
vertical list was already sorted -- so it does more work than
necessary.

Time  : O(N log N)   -- collect O(N) + sort O(N log N) + build O(N)
Space : O(N)          -- array + new list
"""


class BruteForceSolution:
    def _collect_values(self, head, values):
        horizontal = head
        while horizontal:
            vertical = horizontal
            while vertical:
                values.append(vertical.data)
                vertical = vertical.child
            horizontal = horizontal.next

    def _build_child_list(self, values):
        if not values:
            return None
        head = Node(values[0])
        current = head
        for value in values[1:]:
            current.child = Node(value)
            current = current.child
        return head

    def flatten(self, head):
        if head is None:
            return None
        values = []
        self._collect_values(head, values)
        values.sort()
        return self._build_child_list(values)


# =============================================================================
# Approach 2 : Optimal -- Recursion + Merge Two Sorted Lists
# =============================================================================
"""
Reuse "Merge Two Sorted Lists" but swap `next` for `child`. Then
recursively flatten everything to the right before merging the
current list in (see the Golden Observation above for why this
order matters).

Time  : O(N * K)
        N = total nodes, K = number of vertical lists.
        Every merge combines "current list" with "everything
        already flattened," so a node can be touched again in
        each subsequent merge as the flattened list grows --
        not a single linear pass. See Complexity Analysis below.

Space : O(K)  -- recursion stack, one frame per vertical list
"""


def merge(list1, list2):
    """Merge two sorted lists using `child`. O(n1+n2) time, O(1) space."""
    dummy = Node(-1)
    current = dummy

    while list1 and list2:
        if list1.data <= list2.data:
            current.child = list1
            list1 = list1.child
        else:
            current.child = list2
            list2 = list2.child
        current = current.child
        current.next = None  # final list must only use child pointers

    current.child = list1 if list1 else list2
    return dummy.child


class OptimalSolution:
    def flatten(self, head):
        if head is None or head.next is None:
            return head

        merged_head = self.flatten(head.next)
        return merge(head, merged_head)


# =============================================================================
# Dry Run (Optimal only -- brute force is direct/obvious by comparison)
# =============================================================================
"""
3 -> 2 -> 1 -> 4 -> 5   (each with its own vertical child chain)

CALLS go all the way down doing nothing:
    flatten(3) waits on flatten(2) waits on flatten(1)
    waits on flatten(4) waits on flatten(5) -> base case, return 5

RETURNS do all the work, right to left:
    flatten(4): merge(4, 5)        -> 4 5 6 8 9
    flatten(1): merge(1, above)    -> 1 4 5 6 7 8 9 11 12
    flatten(2): merge(2, above)    -> 1 2 4 5 6 7 8 9 10 11 12
    flatten(3): merge(3, above)    -> 1 2 3 4 5 6 7 8 9 10 11 12  (final)
"""


# =============================================================================
# Complexity Comparison
# =============================================================================
"""
Approach       Time            Space   Core idea
------------------------------------------------------------------
Brute Force    O(N log N)      O(N)    ignore sortedness, sort everything
Optimal        O(N * K)        O(K)    flatten right, merge current in

Can we do better than O(N * K)?
Yes -- same idea as Merge K Sorted Lists: push all K "current
head candidates" into a Min Heap instead of repeatedly merging
whole lists. That gets you to O(N log K), same trade-off as that
problem's Optimal solution. The recursive merge above is the
expected interview answer here; reach for the heap version if
asked to push further.
------------------------------------------------------------------

Mental model: don't think "recursion calls recursion." Think
"current list waits for the rest to flatten, then merges itself
in." The recursion only decides merge ORDER, not the merge logic
itself -- that's still just Merge Two Sorted Lists.
"""


if __name__ == "__main__":
    def vertical(vals):
        head = Node(vals[0])
        cur = head
        for v in vals[1:]:
            cur.child = Node(v)
            cur = cur.child
        return head

    n3 = vertical([3])
    n2 = vertical([2, 10])
    n1 = vertical([1, 7, 11, 12])
    n4 = vertical([4, 9])
    n5 = vertical([5, 6, 8])
    n3.next, n2.next, n1.next, n4.next = n2, n1, n4, n5

    expected = list(range(1, 13))
    result = to_list(OptimalSolution().flatten(n3))
    print(result, "OK" if result == expected else "MISMATCH")