import heapq

class Solver(object):
	"""docstring for Solver"""
	def __init__(self, start, goal):
		self.start = start
		self.goal = goal

	def costFunction(self):
		pass

	def solve(self):
		pass

	def getPath(self):
		pass


class PriorityQueue:
	def __init__(self):
		self._queue = []
		self._index = 0

	def insert(self, item, priority):
		heapq.heappush(self._queue, (priority, self._index, item))
		self._index += 1

	def remove(self):
		return heapq.heappop(self._queue)[-1]

	def is_empty(self):
		return len(self._queue) == 0

	def size(self):
		return len(self._queue)
		