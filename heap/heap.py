'''
The C-implementation of heapq runs *very* fast.

However, heapq doesn't support decrease-key/increase-key.

The heap class here is a simple wrapper around heapq with support for
updating the priority as suggested in the doc for heapq.
'''

class heap(object):
	'Heap based on heapq but with support for updating priorities.'
	
	_REMOVED = object() # a sentinel that indicates that an entry has been removed.
	
	def __init__(self,items,priorities=None):
		'''
		Creates a heap from a list of items, and optionally a list of priorities.
		
		If no list of priorities are given, the items themslves are used as priorities.
		'''
		
		from heapq import heapify
		from itertools import count
		
		items = list(items)
		
		if priorities is None:
			# if priorities aren't specified or is None, 
			# we use the items themselves as priorities
			priorities = items
		
		counter = count()
		self._entries = [[priority, next(counter), item] for priority, item in zip(priorities, items)]
		self._entry_finder = {entry[-1]:entry for entry in self._entries}
		self._counter = counter
		
		heapify(self._entries)
	
	def __len__(self):
		# The self._entries is an unreliable way to find the number of entries left as it
		# may be mixed in with yet to remove entries.
		return len(self._entry_finder)
	
	def __contains__(self,item):
		return item in self._entry_finder
	
	def add(self,item,priority=None):
		'Add a new item, or update the priority of an existing item.'
		# Again, as in __init__, if priority is not specified or is None, the item itself
		# serves as the priority.
		from heapq import heappush
		
		if priority is None:
			priority = item
		
		if item in self._entry_finder:
			self.remove(item)
		
		entry = [priority, next(self._counter), item]
		self._entry_finder[item] = entry
		
		heappush(self._entries, entry)
	
	def remove(self,item):
		'Removes an item from the heap. Raises KeyError if not found.'
		# We simply mark as 'to remove', and then later lazily remove the item
		# as we encounter it in pop() or peek().
		self._entry_finder.pop(item)[-1] = self._REMOVED
	
	def pop(self):
		'Remove and return the item with smallest priority value. Raise KeyError if empty.'
		from heapq import heappop
		
		while self._entries:
			priority, count, item = heappop(self._entries)
			if item is not self._REMOVED:
				del self._entry_finder[item]
				return item
				
		# mimic set by raising KeyError if empty.
		raise KeyError('pop from an empty heap')
	
	def peek(self):
		'Peek at smallest item in the heap'
		from heapq import heappop
		
		while self._entries:
			priority, count, item = self._entries[0]
			if item is not self._REMOVED:
				return item
			heappop(self._entries)
		raise KeyError('peek at an empty heap')

	def __repr__(self):
		# showing all the items "as is" might not be the best idea,
		# as some of the items will have self._REMOVED in them.
		# We should filter out all elements that are self._REMOVED and then reheapify.
		# 
		# Of course this is slower than simply returning the list, but converting
		# the list to a string should take at least linear time anyway, so at the very least
		# we are not doing any worse in terms of asymptotic runtime.
		from heapq import heapify
		
		self._entries = [entry for entry in self._entries if entry[-1] is not self._REMOVED]
		heapify(self._entries)
		
		# Immitate the way 'deque' shows things.
		return 'heap('+repr([item for priority, count, item in self._entries])+')'

