class Problem(object):
	"""docstring for Problem"""
	def __init__(self, arg):
		self.arg = arg
		
	class State(object):
		"""Representation of the state"""
		def __init__(self, arg):
			self.arg = arg

		def getNeighbors(self):
			pass

		def getHeuristic(self):
			pass

		def getCost(self):
			pass

	class Action(object):
		def __init__(self, arg):
			self.arg = arg

	def numStates(self):
		pass

	def solve(self):
		pass

	def getPath(self):
		pass

