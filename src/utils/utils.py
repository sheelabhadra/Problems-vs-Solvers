from typing import Dict, List
import heapq
import itertools

"""
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self.count = 0

    def insert(self, item, priority):
        self.count += 1
        heapq.heappush(self._queue, (priority, self.count, item))

    def remove(self):
        return heapq.heappop(self._queue)[-1]

    def is_empty(self):
        return len(self._queue) == 0

    def size(self):
        return len(self._queue)
"""

class PriorityQueue:
    def __init__(self):
        self.pq = []                         # list of entries arranged in a heap
        self.entry_finder = {}               # mapping of tasks to entries
        self.REMOVED = '<removed-task>'      # placeholder for a removed task
        self.counter = itertools.count()     # unique sequence count

    def insert(self, task, priority=0):
        'Add a new task or update the priority of an existing task'
        if task.hash() in self.entry_finder:
            self.delete(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task.hash()] = entry
        heapq.heappush(self.pq, entry)

    def delete(self, task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = self.entry_finder.pop(task.hash())
        entry[-1] = self.REMOVED

    def remove(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.pq:
            priority, count, task = heapq.heappop(self.pq)
            if task is not self.REMOVED:
                del self.entry_finder[task.hash()]
                return task
        raise KeyError('pop from an empty priority queue')

    def peek(self):
        'Look at the lowest priority task. Raise KeyError if empty.'
        i = 0
        while i < len(self.pq):
            priority, count, task = self.pq[i]
            if task is not self.REMOVED:
                return priority
            i += 1
        raise KeyError('peeking into an empty priority queue')

    def is_empty(self):
        return len(self.entry_finder) == 0

    def __len__(self):
        return len(self.entry_finder)
