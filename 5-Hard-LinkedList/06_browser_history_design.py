"""
===============================================================================
                        DESIGN BROWSER HISTORY
===============================================================================

Problem
-------
Design a browser that supports four operations:

1. BrowserHistory(homepage)
2. visit(url)
3. back(steps)
4. forward(steps)

Example

homepage("takeuforward.org")

visit("google.com")
visit("instagram.com")
visit("facebook.com")

back(1)      -> instagram.com
back(1)      -> google.com
forward(1)   -> instagram.com

visit("youtube.com")

Now we CANNOT go to facebook anymore because the forward
history gets deleted.

This is exactly how a real browser works.


Data Structure
--------------
We need to

• Visit a new page
• Move backward
• Move forward

A Doubly Linked List is perfect because every page knows

previous page  <---- current ---->  next page


Pseudo Code
-----------
Browser(homepage)
    Create first node
    current = homepage

visit(url)
    Create a new node
    Connect it after current
    Delete forward history
    Move current to new node

back(steps)
    Move current backward until
        steps become 0
        OR beginning of list is reached

forward(steps)
    Move current forward until
        steps become 0
        OR end of list is reached
===============================================================================
"""


# =============================================================================
# Doubly Linked List Node
# =============================================================================

class Node:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None


# =============================================================================
# Browser History
# =============================================================================

class BrowserHistory:

    # -------------------------------------------------------
    # Constructor
    # -------------------------------------------------------
    def __init__(self, homepage):
        self.current = Node(homepage)

    # -------------------------------------------------------
    # Visit a new page
    # -------------------------------------------------------
    def visit(self, url):

        # Forward history should disappear
        self.current.next = None

        new_node = Node(url)

        new_node.prev = self.current
        self.current.next = new_node

        self.current = new_node

    # -------------------------------------------------------
    # Go back
    # -------------------------------------------------------
    def back(self, steps):

        while steps > 0 and self.current.prev:
            self.current = self.current.prev
            steps -= 1

        return self.current.url

    # -------------------------------------------------------
    # Go forward
    # -------------------------------------------------------
    def forward(self, steps):

        while steps > 0 and self.current.next:
            self.current = self.current.next
            steps -= 1

        return self.current.url


# =============================================================================
# Driver Code
# =============================================================================

browser = BrowserHistory("takeuforward.org")

browser.visit("google.com")
browser.visit("instagram.com")
browser.visit("facebook.com")

print(browser.back(1))         # instagram.com
print(browser.back(1))         # google.com
print(browser.forward(1))      # instagram.com

browser.visit("youtube.com")

print(browser.forward(2))      # youtube.com
print(browser.back(2))         # google.com
print(browser.back(7))         # takeuforward.org


# =============================================================================
# Complexity
# =============================================================================

"""
Constructor
-----------
Time  : O(1)
Space : O(1)

visit()
-------
Time  : O(1)

back(steps)
-----------
Time  : O(steps)

forward(steps)
--------------
Time  : O(steps)

Overall Space
-------------
O(number of pages visited)
"""


# =============================================================================
# Quick Revision
# =============================================================================

"""
✔ Real-world application of Doubly Linked List

Node stores
------------
url
prev
next

Browser stores
--------------
current page

visit()
--------
Create new page
Connect after current
Delete forward history
Move current

back()
-------
Move using prev pointers

forward()
----------
Move using next pointers

This is exactly how browser navigation works.
"""