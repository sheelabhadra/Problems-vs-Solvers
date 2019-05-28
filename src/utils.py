from typing import Dict, List
import heapq

# class PriorityQueue:
#     def __init__(self):
#         self._queue = []
#         self._index = 0

#     def insert(self, item, priority):
#         heapq.heappush(self._queue, (priority, self._index, item))
#         self._index += 1

#     def remove(self):
#         return heapq.heappop(self._queue)[-1]

#     def is_empty(self):
#         return len(self._queue) == 0

#     def size(self):
#         return len(self._queue)

class PriorityQueue:
    def __init__(self):
        self._queue = []

    def insert(self, item, id, priority):
        heapq.heappush(self._queue, (priority, id, item))

    def remove(self):
        return heapq.heappop(self._queue)[-1]

    def is_empty(self):
        return len(self._queue) == 0

    def size(self):
        return len(self._queue)

