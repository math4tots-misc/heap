heap
====

The C-implementation of `heapq` in Python's standard library is very fast.
However `heapq` doesn't support decreas-key/incrase-key.
Following guidelines in [the doc](https://docs.python.org/2/library/heapq.html#priority-queue-implementation-notes), this binary min-heap implementation makes use of the fast `heapq` to supports updating the priority.

NOTE: The code in the doc turns into a fifo queue when priorities are not explicitly specified. In this implementation, if no priorities are explicitly given, the items themselves are used as the priorities.

Perhaps if enough people find `heap` useful, it might be a great additions to `collections` :3

usage
-----
    
Version 0.3 totally changed usage!!!!!

```Python
# The `heap` package contains
# just the one `heap` module which in turn contains
# just the one `heap` class
from heap.heap import heap

# Heaps can be created with either mappings from item -> priorities
h = heap({'b' : 1, 'a' : 2})
h.pop() # 'b'
h.pop() # 'a'

# Or by a list of iterables, in which the element itself represents its priority
h = heap(['a','b'])
h.pop() # 'a'
h.pop() # 'b'

# You can insert new items or update old items with new priorities with __setitem__
h['x'] = 0
h['y'] = 100

# or if you want to use the item itself as its priority, you can use the `add` method
h.add(5)

h.pop() # 'x'
h.pop() # 5
h.peek() # 'y'

# checking whether an element is in a heap is as simple as
('y' in h) # True
('z' in h) # False
# And it's as fast as a single dictionary lookup


```


implementation
--------------

`heap` subclasses directly and only from `collections.Mapping`, and implements exactly the methods

    __init__
    __getitem__
    __setitem__
    __delitem__
    __iter__
    __len__
    __contains__
    __repr__
    keys
    values
    pop
    popitem
    peek
    peekitem
    add
    discard

`heap` also has a class variable

    _REMOVE

for internal use.
