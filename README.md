# Linked List

A structured collection of Linked List problems — starting from the fundamentals and progressing through the core interview patterns. Each problem includes a clean Python implementation with detailed intuition, dry runs, and complexity analysis.

The repository follows **Striver's A2Z DSA Sheet** and is organized by learning progression and problem patterns.

---

## Learn - Singly Linked List

| #   | Topic            | Key Idea                                                      |
| --- | ---------------- | ------------------------------------------------------------- |
| 1   | Node Basics      | Understand nodes, references, and how linked lists are formed |
| 2   | Basic Operations | Traversal, Length, Search, Insertions, and Deletions          |

---

## Learn - Doubly Linked List

| #   | Topic                     | Key Idea                                              |
| --- | ------------------------- | ----------------------------------------------------- |
| 1   | Doubly Linked List Basics | Every node stores both `prev` and `next` pointers     |
| 2   | Basic Operations          | Bidirectional traversal and maintaining both pointers |

---

## Linked List Problems

| #   | Problem                          | Key Idea                                        |
| --- | -------------------------------- | ----------------------------------------------- |
| 1   | Reverse Linked List (Iterative)  | Three-pointer reversal (`prev`, `curr`, `next`) |
| 2   | Reverse Linked List (Recursive)  | Reverse pointers during recursion unwind        |
| 3   | Add Two Numbers                  | Dummy Node + Carry simulation                   |
| 4   | Merge Two Sorted Lists           | Dummy Node for building the answer list         |
| 5   | Odd Even Linked List             | Rearrange odd and even position nodes           |
| 6   | Sort 0s, 1s and 2s               | Counting / Three-list partition                 |
| 7   | Remove Nth Node From End         | Two-pointer gap technique                       |
| 8   | Middle of Linked List            | Slow & Fast Pointer                             |
| 9   | Detect Cycle                     | Floyd's Tortoise & Hare Algorithm               |
| 10  | Length of Cycle                  | Count nodes after cycle detection               |
| 11  | Starting Point of Cycle          | Reset one pointer after first meeting           |
| 12  | Delete Middle Node               | Slow & Fast Pointer with previous node          |
| 13  | Palindrome Linked List           | Middle → Reverse → Compare                      |
| 14  | Add One to Number                | Reverse → Add → Reverse                         |
| 15  | Intersection of Two Linked Lists | Pointer switching technique                     |
| 16  | Sort Linked List                 | Merge Sort on Linked List                       |

---

## Doubly Linked List Problems

| #   | Problem                           | Key Idea                                     |
| --- | --------------------------------- | -------------------------------------------- |
| 1   | Reverse DLL                       | Reverse both `next` and `prev` pointers      |
| 2   | Delete All Occurrences            | Reconnect neighbouring nodes                 |
| 3   | Find Pairs with Given Sum         | Two-pointer technique on DLL                 |
| 4   | Remove Duplicates from Sorted DLL | Skip duplicate nodes while maintaining links |

---

## Hard Linked List

| #   | Problem                               | Key Idea                            |
| --- | ------------------------------------- | ----------------------------------- |
| 1   | Reverse Nodes in K Group              | Reverse fixed-size groups           |
| 2   | Rotate Linked List                    | Find new head using length and tail |
| 3   | Flatten Linked List                   | Merge multiple sorted linked lists  |
| 4   | Merge K Sorted Lists                  | Repeated merge / Heap-based merging |
| 5   | Clone Linked List with Random Pointer | HashMap / Interleaving nodes        |

---

## Structure

The repository is organized into learning modules followed by interview problems.

```text
1-Learn-1D-LinkedList/
2-Learn-Doubly-LinkedList/
3-LinkedList-Problems/
4-Doubly-LinkedList-Problems/
5-Hard-LinkedList/
```

Each problem is implemented as a notebook-style Python file.

```text
N-problem_name.py
```

Every notebook includes:

- Problem Statement
- Intuition
- Brute Force (if applicable)
- Optimal Solution
- Dry Run
- Time & Space Complexity
- Interview Notes

---

## Patterns Covered

- Pointer Reversal
- Dummy Node
- Slow & Fast Pointer
- Two Pointer Gap
- Pointer Manipulation
- Merge Sort on Linked List
- Recursion
- In-place Algorithms
