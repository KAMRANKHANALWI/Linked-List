"""
===============================================================================
              CLONE A LINKED LIST WITH RANDOM POINTER
===============================================================================

Problem
-------
Each node has two pointers:
    next   -> the next node (normal linked list structure)
    random -> ANY node in the list, or None

Return a deep copy of the list. The copy must be completely
independent -- no node in the copy may point into the original.

Pattern: Hashmap-based deep copy, then an O(1)-space three-pass trick
"""


class Node:
    def __init__(self, data, next=None, random=None):
        self.data = data
        self.next = next
        self.random = random


def build_list(pairs):
    """pairs = [(data, random_index_or_None), ...] -> head node.
    random_index refers to the position of another node in `pairs`."""
    nodes = [Node(d) for d, _ in pairs]
    for i, (_, r) in enumerate(pairs):
        nodes[i].next = nodes[i + 1] if i + 1 < len(nodes) else None
        nodes[i].random = nodes[r] if r is not None else None
    return nodes[0] if nodes else None


def to_pairs(head, index_of):
    """head -> [(data, random_index_or_None), ...] for easy comparison."""
    out = []
    current = head
    while current:
        r = index_of.get(current.random) if current.random else None
        out.append((current.data, r))
        current = current.next
    return out


# =============================================================================
# Approach 1 : Brute Force -- HashMap (original node -> copied node)
# =============================================================================
"""
Idea: if we can look up "given this original node, what's its
copy?" in O(1), the rest is easy. A hashmap gives us exactly that.

Pass 1: create a copy of every node (data only), map original -> copy.
Pass 2: for every original node, wire up the copy's `next` and
        `random` by looking up the corresponding copies in the map.

Time  : O(N)  -- two linear passes
Space : O(N)  -- the hashmap holds one entry per node
"""


def copy_random_list_brute(head):
    if head is None:
        return None

    original_to_copy = {}

    current = head
    while current:
        original_to_copy[current] = Node(current.data)
        current = current.next

    current = head
    while current:
        copy = original_to_copy[current]
        copy.next = original_to_copy.get(current.next)
        copy.random = original_to_copy.get(current.random)
        current = current.next

    return original_to_copy[head]


# =============================================================================
# Approach 2 : Optimal -- Interweave, Connect, Separate (O(1) space)
# =============================================================================
"""
Can we avoid the hashmap entirely? Yes -- if we place every copy
node directly next to its original, "the copy of X" becomes just
"X.next". That single fact replaces the whole hashmap.

    original.next  -> the copy of original      (built in Pass 1)
    original.random.next -> the copy of original.random   (used in Pass 2)

Three passes, each doing one job:
    Pass 1: interweave  -- insert copy nodes between originals
    Pass 2: connect      -- wire up the copies' random pointers
    Pass 3: separate      -- unzip into two independent lists

Time  : O(N) total (3 linear passes)
Space : O(1) extra (ignoring the output list itself)
"""


# ---- Pass 1 : interweave a copy after every original -----------------------
"""
7 -> 13 -> 11   becomes   7 -> 7' -> 13 -> 13' -> 11 -> 11'

This is the move that makes everything else O(1): now "the copy
of any node X" is just X.next, no lookup needed.
"""


def insert_copy_in_between(head):
    current = head
    while current:
        copy = Node(current.data)
        copy.next = current.next
        current.next = copy
        current = copy.next


# ---- Pass 2 : connect the copies' random pointers ---------------------------
"""
Golden observation: if original.random points at some node C,
then the COPY of C is just C.next (Pass 1 guarantees this).

    original --random--> C
    copy     --random--> C.next   (== copy of C)

So the entire pass is one line:

    copy.random = original.random.next   (or None, if original.random is None)
"""


def connect_random_pointers(head):
    current = head
    while current:
        copy = current.next
        copy.random = current.random.next if current.random else None
        current = copy.next  # skip the copy, advance to the next original


# ---- Pass 3 : unzip into two independent lists -------------------------------
"""
Think "unzip a zipper." At each step:

    current.next = copy.next          -- restore the original list
    copy.next    = copy.next.next     -- advance the copy list (if it exists)

7 -> 7' -> 13 -> 13' -> 11 -> 11'
becomes
7 -> 13 -> 11        (original, restored)
7' -> 13' -> 11'     (copy, independent)
"""


def separate_lists(head):
    if head is None:
        return None

    current = head
    copied_head = head.next

    while current:
        copy = current.next
        current.next = copy.next
        copy.next = copy.next.next if copy.next else None
        current = current.next

    return copied_head


class OptimalSolution:
    def copy_random_list(self, head):
        if head is None:
            return None

        insert_copy_in_between(head)
        connect_random_pointers(head)
        return separate_lists(head)


# =============================================================================
# Dry Run (Optimal, all three passes on one example)
# =============================================================================
"""
Original:  7 -----> 13 -----> 11
           random:  7->11   13->7   11->None

Pass 1 (interweave):
    7 -> 7' -> 13 -> 13' -> 11 -> 11'
    (copy randoms still None)

Pass 2 (connect randoms via original.random.next):
    7.random  -> 11  =>  11.next = 11'   =>  7'.random  = 11'
    13.random -> 7   =>  7.next  = 7'    =>  13'.random = 7'
    11.random -> None                    =>  11'.random = None

Pass 3 (unzip):
    original.next = copy.next  repeatedly -> 7 -> 13 -> 11
    copy.next = copy.next.next repeatedly -> 7' -> 13' -> 11'

Result: two fully independent lists, copy's randoms correctly
pointing into the copy list only.
"""


# =============================================================================
# Complexity Comparison
# =============================================================================
"""
Approach       Time    Space   Core idea
------------------------------------------------------------------
Brute Force    O(N)    O(N)    hashmap: original node -> copied node
Optimal        O(N)    O(1)    copy sits right after original, so
                                "copy of X" is just X.next -- no lookup
------------------------------------------------------------------

Golden trick, one line:
    copy = original.next

Everything else in the optimal solution -- random-pointer wiring,
list separation -- is just this idea applied twice more.
"""


if __name__ == "__main__":
    # data i, random points to index j (or None)
    spec = [(7, 2), (13, 0), (11, None)]

    # --- Brute force ---
    head1 = build_list(spec)
    nodes1 = []
    c = head1
    while c:
        nodes1.append(c)
        c = c.next
    index_of1 = {n: i for i, n in enumerate(nodes1)}

    clone1 = copy_random_list_brute(head1)
    clone1_nodes = []
    c = clone1
    while c:
        clone1_nodes.append(c)
        c = c.next
    clone1_index = {n: i for i, n in enumerate(clone1_nodes)}

    result1 = to_pairs(clone1, clone1_index)
    no_shared_nodes1 = all(cn not in nodes1 for cn in clone1_nodes)
    print("Brute :", result1, "OK" if result1 == spec and no_shared_nodes1 else "MISMATCH")

    # --- Optimal ---
    head2 = build_list(spec)
    original_nodes = []
    c = head2
    while c:
        original_nodes.append(c)
        c = c.next

    clone2 = OptimalSolution().copy_random_list(head2)

    clone2_nodes = []
    c = clone2
    while c:
        clone2_nodes.append(c)
        c = c.next
    clone2_index = {n: i for i, n in enumerate(clone2_nodes)}

    result2 = to_pairs(clone2, clone2_index)
    no_shared_nodes2 = all(cn not in original_nodes for cn in clone2_nodes)

    # original list must also still be intact after separation
    original_after = []
    c = head2
    while c:
        original_after.append(c.data)
        c = c.next

    ok2 = (result2 == spec and no_shared_nodes2
           and original_after == [d for d, _ in spec])
    print("Optimal:", result2, "OK" if ok2 else "MISMATCH")