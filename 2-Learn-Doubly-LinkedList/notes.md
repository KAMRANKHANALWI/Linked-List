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

### Forward

```python
temp = head

while temp:
    temp = temp.next
```

### Backward

```python
# Reach the last node first

while temp.next:
    temp = temp.next

while temp:
    temp = temp.prev
```

---

## Time Complexity

| Operation          | Time |
| ------------------ | ---- |
| Forward Traversal  | O(n) |
| Backward Traversal | O(n) |
| Length             | O(n) |
| Search             | O(n) |
| Insert Head        | O(1) |
| Insert Tail        | O(n) |
| Insert at Position | O(n) |
| Delete Head        | O(1) |
| Delete Tail        | O(n) |
| Delete at Position | O(n) |

---

## Singly vs Doubly

| Singly       | Doubly                    |
| ------------ | ------------------------- |
| data + next  | data + prev + next        |
| Forward only | Forward & Backward        |
| Less memory  | More memory               |
| Simpler      | Easier insertion/deletion |

---

## Pointer Patterns

### Insert Between Two Nodes

```python
new_node.prev = left
new_node.next = right

left.next = new_node
right.prev = new_node
```

### Delete a Node

```python
left.next = right
right.prev = left
```

---

## Key Takeaway

A Doubly Linked List is just a Singly Linked List with one extra pointer (`prev`).

Remember:

- Move forward using `next`.
- Move backward using `prev`.
- Every insertion updates **both** `next` and `prev`.
- Every deletion reconnects **both** neighboring nodes.
