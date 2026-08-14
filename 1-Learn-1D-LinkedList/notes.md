# Singly Linked List Notes

## What is a Linked List?

A Linked List is a linear data structure where every node stores

- data
- pointer to the next node

Unlike arrays, nodes are not stored contiguously in memory.

---

## Structure

Node
|
|-- data
|-- next

head → first node

---

## Why Linked List?

Advantages

- Dynamic size
- Easy insertion/deletion
- No shifting required

Disadvantages

- No random access
- Extra memory for pointers
- Poor cache locality

---

## Time Complexity

Access           O(N)
Search           O(N)
Insert Head      O(1)
Insert Tail      O(N)
Delete Head      O(1)
Delete Tail      O(N)

---

## Basic Operations

- Traverse
- Search
- Insert
- Delete
- Reverse

---

## Golden Rule

Always save pointers before changing them.

Never lose the remaining list.
