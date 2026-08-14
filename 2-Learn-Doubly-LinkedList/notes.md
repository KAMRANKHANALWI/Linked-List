# Doubly Linked List Notes

## Structure

prev ← data → next

Each node knows

- previous node
- next node

---

## Advantages

- Traverse in both directions
- Easy deletion
- Easy insertion before a node

---

## Disadvantages

- Extra memory
- More pointer updates

---

## Time Complexity

Insert Head      O(1)
Insert Tail      O(1) (with tail pointer)
Delete Node      O(1)

Traversal        O(N)

---

## Pointer Updates

Insertion

prev
next

Deletion

prev.next = next
next.prev = prev

---

## Applications

- Browser History
- Music Player
- Undo / Redo
- LRU Cache
