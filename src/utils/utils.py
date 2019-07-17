from typing import Dict, List
import heapq
import itertools

class PriorityQueue:
    def __init__(self):
        self.pq = []                         # list of entries arranged in a heap
        self.entry_finder = {}               # mapping of tasks to entries
        self.REMOVED = '<removed-task>'      # placeholder for a removed task
        self.counter = itertools.count() 

    def insert(self, task, g=0, h=0):
        'Add a new task or update the priority of an existing task'
        if task in self.entry_finder:
            self.delete(task)
        count = next(self.counter)
        entry = [g+h, (h,g), count, task]
        self.entry_finder[task] = entry
        heapq.heappush(self.pq, entry)

    def delete(self, task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED

    def remove(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.pq:
            priority, order, count, task = heapq.heappop(self.pq)
            if task is not self.REMOVED:
                del self.entry_finder[task]
                return task
        raise KeyError('pop from an empty priority queue')

    def peek(self):
        'Look at the lowest priority task. Raise KeyError if empty.'
        i = 0
        while i < len(self.pq):
            priority, order, count, task = self.pq[i]
            if task is not self.REMOVED:
                return priority
            i += 1
        raise KeyError('peeking into an empty priority queue')

    def is_empty(self):
        return len(self.entry_finder) == 0

    def __len__(self):
        return len(self.entry_finder)
