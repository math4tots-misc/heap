heap
====

heap implementation based on Python's heapq

Python's heapq, when the C-implementation is loaded, is very fast.
However heapq doesn't support decreas-key/incrase-key.
Following guidelines in [the doc](https://docs.python.org/2/library/heapq.html#priority-queue-implementation-notes), this heap implementation supports updating the priority.

NOTE: The code in the doc turns into a fifo queue when priorities are not explicitly specified. In this implementation, if no priorities are explicitly given, the items themselves are used as the priorities.


usage
-----

So far `heap` only implements the methods
    __init__
    __len__
    __contains__
    add
    remove
    pop
    peek

`heap` also has a class variable
  _REMOVE
for internal use.

    
    # The heap module contains just the one class `heap`
    from heap import heap
    
    h = heap([4,2,3])
    
    # heap.add(item,priority=None) adds a new item if item is not already in heap.
    # If the item is already in heap, the method updates the priority.
    # 
    # heap.add(item) # is equivalent to
    # heap.add(item,None) # which is also equivalent to
    # heap.add(item,item)
    
    for i in reversed(range(4,7)):
      h.add(i)
    
    # removing an item is amortized constant time.
    # (items are marked as removed and then actually removed 
    # during calls to `pop` or `peek`)
    h.remove(5)
    
    # checking whether an item is in a heap is as fast as a single dictionary lookup.
    print(6 in h) # True
    print(5 in h) # False
    
    print(h.pop()) # 2

