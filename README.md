# Linked List

A structured collection of Linked List problems — starting from the fundamentals and progressing to interview-level questions. Each problem includes a clean Python implementation with detailed intuition, dry runs, and complexity analysis.

The repository follows **Striver's A2Z DSA Sheet** and is organized by learning progression rather than difficulty alone.

---

## Learn - Singly Linked List

| # | Topic | Key Idea |
|---|--------|----------|
| 1 | Node Basics | Understand nodes, references, and how linked lists are formed |
| 2 | Basic Operations | Traversal, Length, Search, Insertions, Deletions |

---

## Learn - Doubly Linked List

| # | Topic | Key Idea |
|---|--------|----------|
| 1 | Doubly Linked List Basics | Every node stores both `prev` and `next` pointers |
| 2 | Basic Operations | Bidirectional traversal and maintaining both pointers during insertion/deletion |

---

## Medium Linked List

| # | Problem | Key Idea |
|---|---------|----------|
| 1 | Middle of Linked List | Slow & Fast Pointer technique |
| 2 | Reverse Linked List (Iterative) | Three-pointer reversal (`prev`, `curr`, `next`) |
| 3 | Reverse Linked List (Recursive) | Reverse during recursion unwind |
| 4 | Detect Cycle | Floyd's Tortoise & Hare Algorithm |
| 5 | Starting Point of Cycle | Reset one pointer after meeting point |
| 6 | Length of Cycle | Count nodes after cycle detection |
| 7 | Palindrome Linked List | Find middle → Reverse second half → Compare |
| 8 | Odd Even Linked List | Separate odd & even positions, then merge |
| 9 | Remove Nth Node From End | Two-pointer gap technique |
| 10 | Delete Middle Node | Slow & Fast Pointer with previous node |
| 11 | Sort Linked List | Merge Sort on Linked List |
| 12 | Sort 0s, 1s & 2s | Counting / Three-list partition |
| 13 | Intersection of Two Linked Lists | Pointer switching technique |
| 14 | Add One to Number | Reverse → Add → Reverse |
| 15 | Add Two Numbers | Elementary addition with carry |

---

## Medium - Doubly Linked List

| # | Problem | Key Idea |
|---|---------|----------|
| 1 | Delete All Occurrences | Reconnect neighbouring nodes |
| 2 | Find Pairs with Given Sum | Two-pointer technique on DLL |
| 3 | Remove Duplicates from Sorted DLL | Skip duplicate nodes while maintaining links |

---

## Hard Linked List

| # | Problem | Key Idea |
|---|---------|----------|
| 1 | Reverse Nodes in K Group | Reverse fixed-size groups |
| 2 | Rotate Linked List | Find new head using length and tail |
| 3 | Flatten Linked List | Merge multiple sorted linked lists |
| 4 | Clone Linked List with Random Pointer | HashMap / Interleaving nodes |

---

## Structure

Each learning module contains notebook-style Python files with detailed comments.

```
Learn-1D-LinkedList/
Learn-Doubly-LinkedList/
```

Each interview problem is implemented as an individual notebook.

```
N-problem_name.py
```

Every file includes:

- Problem Statement
- Intuition
- Brute Force (if applicable)
- Optimal Solution
- Dry Run
- Time & Space Complexity
- Interview Notes

---

## Topics Covered

singly linked list · doubly linked list · pointer manipulation · slow & fast pointer · linked list reversal · cycle detection · merge sort · recursion · two pointers · in-place algorithms