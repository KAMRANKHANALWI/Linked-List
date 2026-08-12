"""
============================================================
                MERGE K SORTED LINKED LISTS
============================================================

Problem
-------
Given K sorted linked lists, merge them into one sorted list.

L1: 1 -> 4 -> 7
L2: 2 -> 5
L3: 3 -> 6

Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7

Pattern: "K Sorted Sources" -> Min Heap
(same family as Merge K Sorted Arrays, External Merge Sort,
Smallest Range Covering K Lists)

Golden Observation
------------------
Every list is already sorted, so the smallest element of any
list is always its head. That means the next smallest element
of the FINAL answer must be one of the current heads of the
K lists -- never anything deeper.

    Heads: 1, 2, 3  ->  smallest is 1
    Take 1. L1 becomes 4 -> 7.
    Heads: 4, 2, 3  ->  smallest is 2
    ... and so on.

We never need to look at every node -- only the current heads.
Every solution below is just a different way of finding that
smallest head, cheaply.

Notation used throughout this file:
    N = total number of nodes across all lists
    K = number of linked lists
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def build_linked_list(values):
    """[1,2,3] -> 1 -> 2 -> 3"""
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head


def to_list(head):
    out = []
    while head:
        out.append(head.data)
        head = head.next
    return out


# =============================================================================
# Approach 1 : Brute Force -- ignore that the lists are sorted
# =============================================================================
"""
Idea: forget these are linked lists. Dump every value into an
array, sort it, rebuild a fresh list. Works, but throws away
the one fact that makes this problem easy: every input list
was ALREADY sorted.

Time  : O(N log N)   -- collect O(N) + sort O(N log N) + build O(N)
Space : O(N)          -- array + new list
"""


class BruteForceSolution:
    def merge_k_lists(self, lists):
        if not lists:
            return None

        values = []
        for head in lists:
            current = head
            while current:
                values.append(current.data)
                current = current.next

        values.sort()
        return build_linked_list(values)


# =============================================================================
# Approach 2 : Better -- merge lists two at a time
# =============================================================================
"""
Idea: we already know how to merge two sorted lists in O(n1+n2).
Sorted + Sorted = Sorted, so just fold that operation across all
K lists one by one:

    result = merge(L1, L2)
    result = merge(result, L3)
    result = merge(result, L4)
    ...

Why this is better than brute force: no sorting from scratch,
O(1) extra space (we just re-link existing nodes).

Why this still isn't optimal: the merged list keeps growing, so
each successive merge gets more expensive. Let each list average
n = N/K nodes:

    merge 1:  n + n   = 2n
    merge 2:  2n + n  = 3n
    merge 3:  3n + n  = 4n
    ...
    merge K-1: (K-1)n + n = Kn

    total = n(2 + 3 + ... + K) = O(n * K^2) = O((N/K) * K^2) = O(N * K)

Time  : O(N * K)  -- every node can be re-touched once per remaining merge
Space : O(1)      -- reuses existing nodes
"""


def merge_two_sorted(list1, list2):
    """Standard merge two sorted lists. O(n1+n2) time, O(1) space."""
    dummy = Node(-1)
    current = dummy

    while list1 and list2:
        if list1.data <= list2.data:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    current.next = list1 if list1 else list2
    return dummy.next


class BetterSolution:
    def merge_k_lists(self, lists):
        if not lists:
            return None

        merged_head = lists[0]
        for i in range(1, len(lists)):
            merged_head = merge_two_sorted(merged_head, lists[i])
        return merged_head


# =============================================================================
# Approach 3 : Optimal -- Min Heap over the current heads
# =============================================================================
"""
Idea: stop merging whole lists. At any moment we only need to
know the smallest among the K current heads -- so keep exactly
those K candidates in a min heap instead of repeatedly merging
growing lists.

    1. Push the head of every list into the heap.       (size <= K)
    2. Pop the smallest -> attach it to the answer.
    3. If that node has a next node, push it in its place.
    4. Repeat until the heap is empty.

Each node enters and leaves the heap exactly once, and the heap
never holds more than K elements, so each push/pop costs O(log K).

Time  : O(N log K)
Space : O(K)  -- heap holds at most one node per list

This is strictly better than Approach 2 because we replaced
"repeatedly re-merge an ever-growing list" with "always compare
just K candidates."
"""

import heapq


class OptimalSolution:
    def merge_k_lists(self, lists):
        if not lists:
            return None

        heap = []
        for head in lists:
            if head:
                # id(head) is a tiebreaker so heapq never has to
                # compare Node objects when two values are equal.
                heapq.heappush(heap, (head.data, id(head), head))

        dummy = Node(-1)
        current = dummy

        while heap:
            _, _, node = heapq.heappop(heap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(heap, (node.next.data, id(node.next), node.next))

        return dummy.next


# =============================================================================
# Dry Run (Optimal only -- the other two are direct/obvious by comparison)
# =============================================================================
"""
L1: 1 -> 4 -> 7    L2: 2 -> 5    L3: 3 -> 6

heap [1,2,3] -> pop 1, push 4  -> answer: 1
heap [2,3,4] -> pop 2, push 5  -> answer: 1 2
heap [3,4,5] -> pop 3, push 6  -> answer: 1 2 3
heap [4,5,6] -> pop 4, push 7  -> answer: 1 2 3 4
heap [5,6,7] -> pop 5           -> answer: 1 2 3 4 5
heap [6,7]   -> pop 6           -> answer: 1 2 3 4 5 6
heap [7]     -> pop 7           -> answer: 1 2 3 4 5 6 7
heap []      -> done
"""


# =============================================================================
# Complexity Comparison
# =============================================================================
"""
Approach       Time            Space   Core idea
------------------------------------------------------------------
Brute Force    O(N log N)      O(N)    ignore sortedness, sort everything
Better         O(N * K)        O(1)    merge two lists at a time
Optimal        O(N log K)      O(K)    min heap over current heads only
------------------------------------------------------------------

Mental model: don't think "merge K lists." Think "I have K sorted
sources, I only ever need the smallest current candidate from
each source" -- that reframing is what leads straight to the heap.
"""


if __name__ == "__main__":
    tests = [
        [[1, 4, 7], [2, 5], [3, 6]],
        [[1, 4, 7], [], [3, 6]],
        [[], [], []],
        [],
        [[5], [5], [5]],
        [[1, 1, 2], [1, 1, 3]],
    ]

    for t in tests:
        expected = sorted(x for sub in t for x in sub)
        results = []
        for Solution in (BruteForceSolution, BetterSolution, OptimalSolution):
            lists = [build_linked_list(v) for v in t]
            results.append(to_list(Solution().merge_k_lists(lists)))

        ok = all(r == expected for r in results)
        print(t, "->", results, "OK" if ok else "MISMATCH")