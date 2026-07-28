# Floyd's Cycle Detection Algorithm (Tortoise & Hare)

---

## The Goal

Suppose we have a linked list like this.

```text
Head

↓

1 → 2 → 3 → 4 → 5
          ↑     ↓
          8 ← 7 ←6
```

We want to answer three questions:

1. Does a cycle exist?
2. What is the length of the cycle?
3. Where does the cycle begin?

Surprisingly, **all three questions can be answered using the same algorithm**.

This algorithm is known as **Floyd's Cycle Detection Algorithm**, or more commonly,

> **The Tortoise and the Hare Algorithm**

---

# Step 1 — Forget Linked Lists

Instead, imagine a circular running track.

```text
          ◯
       /     \
     /         \
    |           |
     \         /
       \_____/
```

Two runners start at the same point.

🐢 Slow Runner

- Moves **1 step every second**

🐇 Fast Runner

- Moves **2 steps every second**

Question:

> Will the fast runner eventually catch the slow runner?

Let's see.

---

Second 0

```text
🐢🐇
●---------------------------●
```

---

Second 1

```text
🐢----🐇
```

Fast is ahead.

---

Second 2

```text
🐢--------🐇
```

Still ahead.

---

Second 3

```text
🐇
🐢
```

They meet.

Why?

Because every second,

Fast gains exactly **one step** on Slow.

If the track has **L nodes**,

after at most **L moves**, Fast must catch Slow.

This is the core idea behind Floyd's Algorithm.

---

# Step 2 — Add the Tail

A linked list isn't just a cycle.

It has two parts.

```text
Head

↓

1 → 2 → 3 → 4 → 5
          ↑     ↓
          8 ← 7 ←6
```

We can split it into

```text
Tail

+

Cycle
```

Like this.

```text
Head

↓

1 → 2 → 3

↓

Cycle

4 → 5 → 6 → 7 → 8
↑               ↓
└───────────────┘
```

---

# Step 3 — Can They Meet Before the Cycle?

Suppose both pointers are still inside the tail.

```text
Head

↓

1 → 2 → 3
```

Can they meet?

No.

Why?

Because the tail is just a straight path.

Fast is always ahead.

There is no way for Fast to "lap" Slow.

So,

> **The first meeting can never happen before entering the cycle.**

The meeting is guaranteed to happen **inside the cycle**.

---

# Step 4 — Once Inside the Cycle

Forget the tail again.

We're back to runners on a circular track.

```text
        ◯
     /     \
    |       |
     \_____/
```

Since Fast gains one node every move,

the gap keeps shrinking.

Eventually,

```text
Slow == Fast
```

A meeting is guaranteed.

This answers our first question.

✔ Cycle detected.

---

# Step 5 — Finding the Length of the Cycle

Once Slow and Fast meet,

freeze one pointer.

Move the other pointer around the cycle until it returns.

```text
Meeting Point

↓

4 → 5 → 6
↑       ↓
└───────┘
```

Count the steps.

That's the cycle length.

Simple.

---

# Step 6 — The Hard Question

How do we find **where the cycle begins?**

Suppose

```text
x = Distance from Head to Cycle Start

y = Distance from Cycle Start to Meeting Point

L = Length of the Cycle
```

Diagram

```text
Head

|

|------ x ------|

↓

C -------- M
|          |
|          |
|          |
+----------+
```

where

- C = Cycle Start
- M = Meeting Point

---

# Step 7 — The Mathematics

When Slow and Fast meet,

Slow travelled

```text
x + y
```

Fast travelled

```text
x + y + kL
```

where

```text
k ≥ 1
```

because Fast completed one or more extra loops.

Since Fast moves twice as fast,

```text
2(x + y)

=

x + y + kL
```

Subtract both sides.

```text
x + y = kL
```

Rearrange.

```text
x = kL - y
```

This tiny equation explains the entire algorithm.

---

# Step 8 — The Magic

Look carefully.

Distance from Head to Cycle Start

```text
x
```

Distance from Meeting Point back to Cycle Start

```text
kL - y
```

But

```text
x = kL - y
```

They are exactly the same distance.

So,

Place one pointer here.

```text
Head
```

Place the other here.

```text
Meeting Point
```

Move both

**one step at a time.**

After exactly **x moves**,

both pointers arrive at

```text
Cycle Start
```

at the same time.

This is why Floyd's Algorithm works.

No guessing.

No magic.

Just mathematics.

---

# Visual Summary

```text
                M
              ●───────●
            /           \
          /               \
         ●                 ●
         C                 |
          \               /
            \___________/

Head
  |
  |
  |
  ●
```

Distance

```text
Head → C

=

Meeting → C
(along the cycle)
```

Move both pointers together.

They meet exactly at **C**.

---

# Complexity

| Problem | Time | Space |
|----------|------|-------|
| Detect Cycle | O(n) | O(1) |
| Length of Cycle | O(n) | O(1) |
| Starting Point of Cycle | O(n) | O(1) |

---

# Key Takeaways

✅ Floyd's Algorithm uses two pointers.

✅ Slow moves one step.

✅ Fast moves two steps.

✅ They always meet if a cycle exists.

✅ One full traversal from the meeting point gives the cycle length.

✅ Reset one pointer to the head and move both one step at a time.

✅ They meet exactly at the starting point of the cycle.

---

## Final Thought

At first, Floyd's Algorithm feels like a clever trick.

But once you realise that the linked list can be viewed as a **straight path followed by a circular running track**, everything becomes intuitive.

The algorithm isn't magic.

It's simply the inevitable consequence of two runners moving at different speeds on a loop.