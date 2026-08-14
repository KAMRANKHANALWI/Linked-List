# Floyd's Cycle Detection Algorithm (Tortoise & Hare)

## Problem Statement

Given a linked list, determine:
1. Whether it contains a cycle
2. The length of the cycle (if one exists)
3. The starting node of the cycle (if one exists)

All three can be answered using **one algorithm** — two pointers moving at different speeds.

```text
1 → 2 → 3 → 4 → 5
          ↑     ↓
          8 ← 7 ← 6
```

---

## Intuition

Picture two runners on a circular track:

- 🐢 **Slow** moves 1 step at a time
- 🐇 **Fast** moves 2 steps at a time

Every step, Fast closes the gap to Slow by exactly 1 node. If the track (cycle) has `L` nodes, Fast is guaranteed to catch Slow within at most `L` moves. This is the entire basis for cycle detection.

A linked list isn't a pure cycle, though — it's a **tail leading into a cycle**:

```text
Head → 1 → 2 → 3 → [Cycle: 4 → 5 → 6 → 7 → 8 → back to 4]
```

**Claim:** Slow and Fast can never meet while still on the tail.

The tail is a straight path — Fast is always strictly ahead of Slow in node count there, so it can't "lap" Slow. A meeting is only possible once both pointers are inside the cycle, where lapping is geometrically possible. So detection alone (Step 1) is guaranteed to work: if a cycle exists, the two pointers **will** meet inside it.

---

## Step 1: Detect a Cycle

```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

**Why it works:** if there's no cycle, `fast` hits `None` and the loop ends. If there is a cycle, the gap between `slow` and `fast` shrinks by 1 every iteration, so they must eventually collide.

---

## Step 2: Find the Cycle Length

Once `slow` and `fast` meet, freeze one pointer and walk the other around the cycle, counting steps until it returns to the meeting point.

```python
def cycle_length(meeting_point):
    length = 1
    ptr = meeting_point.next
    while ptr != meeting_point:
        ptr = ptr.next
        length += 1
    return length
```

---

## Step 3: Find the Starting Point of the Cycle

This is the part that looks like magic until you do the algebra.

### Setup

| Symbol | Meaning |
|---|---|
| `x` | Distance from Head to Cycle Start (`C`) |
| `y` | Distance from `C` to the Meeting Point (`M`), along the cycle |
| `L` | Length of the cycle |

```text
Head ──(x steps)──▶ C ──(y steps)──▶ M
                     ▲                │
                     └──(L steps)─────┘
```

### The Derivation

When `slow` and `fast` meet:

- `slow` has travelled: `x + y`
- `fast` has travelled: `x + y + kL`, for some integer `k ≥ 1` (fast completed `k` extra full loops before catching up)

Since `fast` moves at twice the speed of `slow`, the distance `fast` covers is always exactly `2×` what `slow` covers, **at every point in time** — including the moment they meet:

```text
2(x + y) = x + y + kL
```

Solving:

```text
x + y = kL
x = kL - y
```

### Why This Matters

`x` is the distance from **Head** to `C`.
`kL - y` is the distance from **M** to `C`, if you walk forward `k` times around the cycle from `M`.

Since walking `L` steps from any point in the cycle returns you to the same point, walking `kL - y` steps from `M` lands in exactly the same place as walking `L - y` steps — the extra `(k-1)L` is just looping in place. So `kL - y` and `x` describe the **same physical distance to `C`**, just expressed differently.

**This means:** if you place one pointer at `Head` and another at `M`, and move both **one step at a time**, they will reach `C` simultaneously — after exactly `x` steps.

```python
def find_cycle_start(head, meeting_point):
    ptr1 = head
    ptr2 = meeting_point
    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    return ptr1  # this is C
```

### Worked Example

Take `x = 2`, `y = 3`, `L = 5`, `k = 1`:

- `slow` travels `x + y = 5` steps to reach `M`
- `fast` travels `x + y + kL = 10` steps to reach `M` — exactly `2×` slow's distance ✔
- `x = kL - y = 5 - 3 = 2` ✔, matching the actual head-to-`C` distance

Now walk both pointers one step at a time:
- From `Head`: 2 steps → reaches `C`
- From `M`: 2 steps → reaches `C` (since `M` is 3 steps into a 5-length cycle, 2 more steps completes the lap back to `C`)

Both arrive at `C` after exactly 2 steps. ✔

---

## Complexity

| Problem | Time | Space |
|---|---|---|
| Detect Cycle | `O(n)` | `O(1)` |
| Length of Cycle | `O(n)` | `O(1)` |
| Starting Point of Cycle | `O(n)` | `O(1)` |

---

## Key Takeaways

- Two pointers, moving at speeds `1` and `2`, always meet inside a cycle if one exists — they can never meet on the tail.
- The meeting point alone gives you the cycle length via a single extra traversal.
- The identity `x = kL - y` is what makes the "reset one pointer to head" trick work — it's not a coincidence, it falls straight out of the fact that `fast` moves exactly twice as fast as `slow`.