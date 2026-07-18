# Basic Operations - Singly Linked List

## Golden Traversal Pattern

```python
temp = head

while temp:
    # Work

    temp = temp.next
```

Everything in a Linked List is just traversal + some logic.

---

## Time Complexity

| Operation | Time |
|-----------|------|
| Traverse | O(n) |
| Length | O(n) |
| Search | O(n) |
| Insert Head | O(1) |
| Insert Tail | O(n) |
| Insert Position | O(n) |
| Delete Head | O(1) |
| Delete Tail | O(n) |
| Delete Position | O(n) |

---

## Common Patterns

### Traverse

```python
temp = head

while temp:
    temp = temp.next
```

---

### Count

```python
count += 1
```

---

### Search

```python
if temp.data == value:
    return True
```

---

### Insert at Head

```python
new.next = head
head = new
```

---

### Delete Head

```python
head = head.next
```

---

### Insert at Tail

```python
while temp.next:
    temp = temp.next
```

---

### Delete Tail

```python
while temp.next.next:
    temp = temp.next
```

---

## Interview Tips

- Head insertion is **O(1)** because no traversal is needed.
- Tail insertion is **O(n)** unless a tail pointer is maintained.
- Always handle the edge cases:
  - Empty list
  - Single-node list
  - Head position
- Never lose the `head` reference during traversal—use a temporary pointer (`temp`).

---

## Biggest Takeaway

Every linked list algorithm follows the same recipe:

1. Start from `head`.
2. Traverse using a temporary pointer.
3. Perform the required operation.
4. Update links carefully without losing nodes.