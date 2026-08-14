# Linked List

A structured, notebook-style walkthrough of Linked List concepts and interview problems — from fundamentals to the hardest patterns asked in interviews.

Built while following **Striver's A2Z DSA Sheet**. Every problem is implemented in Python with intuition, dry runs, and complexity analysis, so the repo doubles as a long-term revision resource, not just a solved-problems dump.

![Language](https://img.shields.io/badge/language-Python-blue)
![Sheet](https://img.shields.io/badge/reference-Striver's%20A2Z-orange)
![Problems](https://img.shields.io/badge/problems-26-brightgreen)

---

## Why this repo

Most DSA repos are just code dumps — a solution file with no explanation of _why_ it works. This one is built to be readable months later:

- Every notebook follows the same format: **Problem → Intuition → Brute Force → Optimal → Dry Run → Complexity → Interview Notes**
- Concepts are separated from problems, so fundamentals aren't buried among interview questions
- Patterns are explicitly labeled, so revision is pattern-first, not problem-first

---

## Learn — Singly Linked List

| #   | Topic            | Key Idea                                                      |
| --- | ---------------- | ------------------------------------------------------------- |
| 1   | Node Basics      | Understand nodes, references, and how linked lists are formed |
| 2   | Basic Operations | Traversal, length, search, insertions, and deletions          |

## Learn — Doubly Linked List

| #   | Topic                     | Key Idea                                              |
| --- | ------------------------- | ----------------------------------------------------- |
| 1   | Doubly Linked List Basics | Every node stores both `prev` and `next` pointers     |
| 2   | Basic Operations          | Bidirectional traversal and maintaining both pointers |

---

## Linked List Problems

| #   | Problem                          | Key Idea                                             |
| --- | -------------------------------- | ---------------------------------------------------- |
| 1   | Reverse Linked List (Iterative)  | Three-pointer reversal (`prev`, `curr`, `next`)      |
| 2   | Reverse Linked List (Recursive)  | Reverse pointers during recursion unwind             |
| 3   | Add Two Numbers                  | Dummy node + carry simulation                        |
| 4   | Merge Two Sorted Lists           | Dummy node for building the answer list              |
| 5   | Odd Even Linked List             | Rearrange odd- and even-position nodes               |
| 6   | Sort 0s, 1s and 2s               | Counting / three-list partition                      |
| 7   | Remove Nth Node From End         | Two-pointer gap technique                            |
| 8   | Middle of Linked List            | Slow & fast pointer                                  |
| 9   | Detect Cycle                     | Floyd's Tortoise & Hare algorithm                    |
| 10  | Length of Cycle                  | Count nodes after cycle detection                    |
| 11  | Starting Point of Cycle          | Reset one pointer after first meeting                |
| 12  | Delete Middle Node               | Slow & fast pointer with a trailing previous pointer |
| 13  | Palindrome Linked List           | Find middle → reverse second half → compare          |
| 14  | Add One to Number                | Reverse → add → reverse                              |
| 15  | Intersection of Two Linked Lists | Pointer-switching technique                          |
| 16  | Sort Linked List                 | Merge sort on a linked list                          |

## Doubly Linked List Problems

| #   | Problem                           | Key Idea                                     |
| --- | --------------------------------- | -------------------------------------------- |
| 1   | Reverse DLL                       | Reverse both `next` and `prev` pointers      |
| 2   | Delete All Occurrences            | Reconnect neighbouring nodes                 |
| 3   | Find Pairs with Given Sum         | Two-pointer technique on a DLL               |
| 4   | Remove Duplicates from Sorted DLL | Skip duplicate nodes while maintaining links |

## Hard Linked List

| #   | Problem                               | Key Idea                                       |
| --- | ------------------------------------- | ---------------------------------------------- |
| 1   | Reverse Nodes in K Group              | Reverse fixed-size groups                      |
| 2   | Rotate Linked List                    | Find the new head using length and tail        |
| 3   | Flatten Linked List                   | Merge multiple sorted linked lists             |
| 4   | Merge K Sorted Lists                  | Sequential merge / min-heap                    |
| 5   | Clone Linked List with Random Pointer | HashMap / interweaving nodes                   |
| 6   | Browser History Design _(Bonus)_      | Real-world application of a doubly linked list |

---

## Repository Structure

```text
LINKED_LIST/
│
├── README.md
│
├── 1-Learn-1D-LinkedList/
├── 2-Learn-Doubly-LinkedList/
├── 3-LinkedList-Problems/
├── 4-Doubly-LinkedList-Problems/
└── 5-Hard-LinkedList/
```

Each module contains:

- Notebook-style Python implementations
- A `notes.md` for quick revision and pattern summaries

Each notebook includes:

- Problem statement
- Intuition
- Brute force (if applicable)
- Optimal solution
- Dry run
- Time & space complexity
- Interview notes

---

## Patterns Covered

`Pointer Reversal` · `Dummy Node` · `Pointer Manipulation` · `Slow & Fast Pointer` · `Two-Pointer Gap` · `Merge Pattern` · `Merge Sort` · `Recursion` · `Random Pointer` · `In-place Algorithms`
