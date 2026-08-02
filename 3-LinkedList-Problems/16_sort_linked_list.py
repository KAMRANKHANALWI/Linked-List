"""
===============================================================================
                           SORT LINKED LIST
===============================================================================

Problem Statement
-----------------

Given the head of a singly linked list, sort the linked list in ascending order
and return the head of the sorted list.

You must achieve

    Time Complexity  : O(n log n)

    Space Complexity : O(1) Auxiliary Space
                       (Ignoring recursion stack)

Example 1

Input

4 → 2 → 1 → 3

Output

1 → 2 → 3 → 4


Example 2

Input

-1 → 5 → 3 → 4 → 0

Output

-1 → 0 → 3 → 4 → 5


===============================================================================
Golden Observation
===============================================================================

Arrays have Random Access.

Linked Lists DO NOT.

Because of this...

Algorithms like

• Quick Sort
• Heap Sort

are NOT ideal for Linked Lists.

Instead...

Merge Sort becomes the perfect algorithm because

1. Splitting a linked list is easy.
2. Merging two sorted linked lists is easy.
3. No random indexing is required.

This is why almost every interview expects Merge Sort.

===============================================================================
Quick Algorithm (30 Second Revision)
===============================================================================

mergeSort(head)

1. If list has 0 or 1 node

       return head

2. Find middle node

3. Split list into

       Left Half
       Right Half

4. Sort left recursively

5. Sort right recursively

6. Merge both sorted halves

7. Return merged list

===============================================================================
Quick Pseudo Code
===============================================================================

mergeSort(head)

{

    if head == NULL or head.next == NULL

        return head

    middle = findMiddle(head)

    left = head

    right = middle.next

    middle.next = NULL

    left = mergeSort(left)

    right = mergeSort(right)

    return merge(left, right)

}

===============================================================================
Recursive Flow
===============================================================================

                mergeSort(head)

                       |

          ----------------------------

          |                          |

   mergeSort(left)          mergeSort(right)

          |                          |

          -------- Merge -------------

                     |

              Sorted Linked List

===============================================================================
Why Merge Sort Works?
===============================================================================

Large problems are difficult.

Small problems are easy.

Merge Sort repeatedly breaks

        8 nodes

into

        4 + 4

then

        2 + 2

then

        1 + 1

A single node is already sorted.

Now simply merge them back.

Exactly like assembling LEGO blocks.

===============================================================================
Approach 1 : Brute Force (Using Array)
===============================================================================

Idea

Step 1

Traverse the linked list.

Store every value inside an array.

Step 2

Sort the array.

Step 3

Traverse the linked list again.

Overwrite every node with the sorted values.

Visualization

Linked List

4 → 2 → 1 → 3

↓

Array

[4,2,1,3]

↓

Sort

[1,2,3,4]

↓

Rewrite Linked List

1 → 2 → 3 → 4

Time Complexity

Traversing LL      = O(n)

Sorting Array      = O(n log n)

Rewrite LL         = O(n)

Total

O(n log n)

Space Complexity

O(n)

Extra array required.

===============================================================================
Approach 2 : Optimal (Merge Sort)
===============================================================================

Instead of copying values,

we actually rearrange the node links.

No extra array.

Just recursion.

The algorithm consists of THREE helper functions

1. find_middle()

Splits the linked list.

2. merge()

Merges two sorted linked lists.

3. merge_sort()

Recursive Divide & Conquer.

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
# Linked List
# =============================================================================


class LinkedList:

    def __init__(self):
        self.head = None

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

    # -------------------------------------------------------------------------
    # Traverse
    # -------------------------------------------------------------------------

    def traverse(self):

        temp = self.head

        while temp:

            print(temp.data, end=" -> ")

            temp = temp.next

        print("None")

    # -------------------------------------------------------------------------
    # Brute Force
    # -------------------------------------------------------------------------

    def sort_brute(self):

        values = []

        temp = self.head

        while temp:

            values.append(temp.data)

            temp = temp.next

        values.sort()

        temp = self.head

        index = 0

        while temp:

            temp.data = values[index]

            index += 1

            temp = temp.next

    # =========================================================================
    # Quick Revision : Find Middle
    # =========================================================================
    #
    # slow = head
    # fast = head.next
    #
    # while fast and fast.next
    #
    #       slow = slow.next
    #       fast = fast.next.next
    #
    # return slow
    #
    # Why fast = head.next ?
    #
    # We intentionally return the FIRST middle node.
    #
    # Example
    #
    # 1 → 2 → 3 → 4
    #
    # returns
    #
    # 2
    #
    # instead of 3.
    #
    # This makes splitting easier.
    #
    # =========================================================================

    def find_middle(self, head):

        slow = head
        fast = head.next

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        return slow

    # =========================================================================
    # Quick Revision : Merge Two Sorted Linked Lists
    # =========================================================================
    #
    # dummy = Node()
    #
    # tail = dummy
    #
    # while left and right
    #
    #       attach smaller node
    #
    #       move that pointer
    #
    #       move tail
    #
    # attach remaining nodes
    #
    # return dummy.next
    #
    # =========================================================================

    def merge(self, left, right):

        dummy = Node(-1)

        tail = dummy

        while left and right:

            if left.data <= right.data:

                tail.next = left
                left = left.next

            else:

                tail.next = right
                right = right.next

            tail = tail.next

        # One list may still contain nodes.
        # Since it is already sorted,
        # simply attach it.

        if left:

            tail.next = left

        else:

            tail.next = right

        return dummy.next

    # =========================================================================
    # Recursive Flow (30 Second Revision)
    # =========================================================================
    #
    # mergeSort(head)
    #
    # Base Case
    #
    #       if 0 or 1 node
    #
    #              return head
    #
    # -----------------------------
    #
    # Find Middle
    #
    # Split
    #
    # left  = head
    #
    # right = middle.next
    #
    # middle.next = None
    #
    # -----------------------------
    #
    # Sort both halves
    #
    # left  = mergeSort(left)
    #
    # right = mergeSort(right)
    #
    # -----------------------------
    #
    # Merge
    #
    # return merge(left,right)
    #
    # =========================================================================

    def merge_sort(self, head):

        # Base Case
        #
        # Empty List
        #
        # OR
        #
        # Single Node
        #
        # Already Sorted

        if head is None or head.next is None:

            return head

        # ------------------------------------------------------------
        # Step 1
        #
        # Find the FIRST middle node.
        # ------------------------------------------------------------

        middle = self.find_middle(head)

        # ------------------------------------------------------------
        # Step 2
        #
        # Split the linked list.
        #
        # Before
        #
        # 4 -> 2 -> 1 -> 3
        #
        #          ^
        #        middle
        #
        # After
        #
        # Left
        #
        # 4 -> 2
        #
        # Right
        #
        # 1 -> 3
        # ------------------------------------------------------------

        left = head

        right = middle.next

        middle.next = None

        # ------------------------------------------------------------
        # Step 3
        #
        # Recursively sort both halves.
        # ------------------------------------------------------------

        left = self.merge_sort(left)

        right = self.merge_sort(right)

        # ------------------------------------------------------------
        # Step 4
        #
        # Merge the two sorted halves.
        # ------------------------------------------------------------

        return self.merge(left, right)

    # -------------------------------------------------------------------------
    # Sort Linked List
    # -------------------------------------------------------------------------

    def sort_optimal(self):

        self.head = self.merge_sort(self.head)


# =============================================================================
# Driver Code
# =============================================================================

if __name__ == "__main__":

    ll = LinkedList()

    ll.insert_tail(4)
    ll.insert_tail(2)
    ll.insert_tail(1)
    ll.insert_tail(3)
    ll.insert_tail(5)

    print("Original Linked List")
    ll.traverse()

    print("\nSorting Using Merge Sort...\n")

    ll.sort_optimal()

    print("Sorted Linked List")
    ll.traverse()


"""
===============================================================================
Dry Run
===============================================================================

Input

4 → 2 → 1 → 3 → 5

---------------------------------------------
Step 1

Find Middle

4 → 2 → 1 → 3 → 5
        ↑

Left

4 → 2 → 1

Right

3 → 5

---------------------------------------------
Sort Left

4 → 2 → 1

↓

Split

4 → 2

1

↓

Split

4

2

↓

Merge

2 → 4

↓

Merge

1 + (2 → 4)

↓

1 → 2 → 4

---------------------------------------------
Sort Right

3 → 5

↓

Split

3

5

↓

Merge

3 → 5

---------------------------------------------
Final Merge

Left

1 → 2 → 4

Right

3 → 5

Compare

1 ✓

2 ✓

3 ✓

4 ✓

5

Answer

1 → 2 → 3 → 4 → 5

===============================================================================
Recursion Tree
===============================================================================

                    4 2 1 3 5

                  /           \

             4 2 1             3 5

            /     \           /   \

          4 2      1         3     5

         /   \

        4     2


Now Merge

4 + 2

↓

2 4

↓

2 4 + 1

↓

1 2 4

↓

3 + 5

↓

3 5

↓

1 2 4 + 3 5

↓

1 2 3 4 5

===============================================================================
Time Complexity
===============================================================================

Finding Middle

O(n)

Merging

O(n)

Levels of Recursion

log n

Overall

O(n log n)

===============================================================================
Space Complexity
===============================================================================

Auxiliary Space

O(1)

Recursion Stack

O(log n)

Therefore

Overall

O(log n)

===============================================================================
Why Merge Sort is Perfect for Linked Lists
===============================================================================

Arrays

✓ Random Access

✓ Quick Sort works well

✓ Heap Sort works well

------------------------------------------------

Linked Lists

✗ No Random Access

✗ Swapping nodes is expensive

✓ Splitting is easy

✓ Merging is easy

Therefore

Merge Sort is the natural choice.

===============================================================================
Pattern Recognition
===============================================================================

This problem combines FOUR famous interview patterns.

✓ Slow & Fast Pointer

Used to find the middle.

------------------------------------------------

✓ Divide & Conquer

Break one big problem into two smaller problems.

------------------------------------------------

✓ Recursion

Sort left.

Sort right.

Merge.

------------------------------------------------

✓ Dummy Node

Used while merging two sorted linked lists.

===============================================================================
30 Second Mental Checklist
===============================================================================

□ Base Case

head == None

OR

head.next == None

-------------------------------------

□ Find FIRST Middle

slow = head

fast = head.next

-------------------------------------

□ Split

right = middle.next

middle.next = None

-------------------------------------

□ Recursive Calls

left = mergeSort(left)

right = mergeSort(right)

-------------------------------------

□ Merge

merge(left, right)

-------------------------------------

□ Return

merged linked list

===============================================================================
Common Mistakes
===============================================================================

❌ Forgetting

middle.next = None

Both recursive calls receive the same linked list.

Infinite recursion.

------------------------------------------------

❌ Using

fast = head

instead of

fast = head.next

For even-sized lists this returns the SECOND middle.

Splitting becomes unbalanced.

------------------------------------------------

❌ Forgetting to attach remaining nodes
after the merge loop.

One half of the list gets lost.

------------------------------------------------

❌ Returning dummy instead of dummy.next.

===============================================================================
Takeaways
===============================================================================

Whenever you see

• Sort Linked List

Immediately think

Merge Sort.

------------------------------------------------

Whenever you need

• Split Linked List

Think

Slow + Fast Pointer.

------------------------------------------------

Whenever you need

• Merge Two Sorted Lists

Think

Dummy Node Pattern.

------------------------------------------------

Together these three patterns solve the entire problem.

===============================================================================
Related Problems
===============================================================================

✓ Merge Two Sorted Lists

✓ Merge K Sorted Lists

✓ Middle of Linked List

✓ Split Linked List

✓ Convert Sorted List to BST

✓ Inversion Count (Merge Sort on Arrays)

✓ Reverse Linked List

===============================================================================
"""
