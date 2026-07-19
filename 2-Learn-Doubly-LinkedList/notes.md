# Doubly Linked List - Notes

## Node Structure

```python
class Node:
    data
    prev
    next
```

---

## Golden Rule

Every connection requires **two updates**.

```python
current.next = new_node
new_node.prev = current
```

Every disconnection also requires **two updates**.

```python
current.next = next_node
next_node.prev = current
```

---

## Traversal

Forward

```python
temp = head

while temp:
    temp = temp.next
```

Backward

```python
while temp:
    temp = temp.prev
```

---

## Time Complexity

| Operation | Time |
|----------|------|
| Forward Traversal | O(n) |
| Backward Traversal | O(n) |
| Length | O(n) |
| Search | O(n) |
| Insert Head | O(1) |
| Insert Tail | O(n) |
| Delete Head | O(1) |
| Delete Tail | O(n) |

---

## Singly vs Doubly

| Singly | Doubly |
|--------|---------|
| data + next | data + prev + next |
| Forward only | Forward & Backward |
| Less memory | More memory |
| Simpler | Easier insertion/deletion |

---

## Key Takeaway

A Doubly Linked List is just a Singly Linked List with one extra pointer (`prev`).

The only thing to remember is:

- During insertion, update both `next` and `prev`.
- During deletion, reconnect both neighboring nodes.