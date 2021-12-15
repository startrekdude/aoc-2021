from collections import Counter
from sys import argv as args, maxsize

path = args[1] if len(args) >= 2 else "sample-input.txt"
with open(path) as f:
	lines = f.read().splitlines()

risks = [[int(x) for x in line] for line in lines]
width = len(risks[0])
height = len(risks[1])

vertices = {}

class Vertex:
	@staticmethod
	def at(y, x):
		if (y, x) in vertices:
			return vertices[y, x]
		vertices[y, x] = Vertex(y, x)
		return vertices[y, x]
	
	def __init__(self, y, x):
		self.y = y
		self.x = x
		self.risk = risks[y][x]
		self.path_risk = maxsize
	
	def __repr__(self):
		return repr(self.__dict__)
	
	def adjacent(self):
		candidates = (
			(self.y + 1, self.x),
			(self.y - 1, self.x),
			(self.y, self.x + 1),
			(self.y, self.x - 1),
		)
		for y, x in candidates:
			if 0 <= y < height and 0 <= x < height:
				yield Vertex.at(y, x)

def score_paths(start):
	queue = {start}
	while queue:
		next_queue = set()
		
		for visit in queue:
			for vertex in visit.adjacent():
				if vertex.path_risk > vertex.risk + visit.path_risk:
					vertex.path_risk = vertex.risk + visit.path_risk
					next_queue.add(vertex)
		
		queue = next_queue

start = Vertex.at(0, 0)
start.path_risk = 0
score_paths(start)

end = Vertex.at(height - 1, width - 1)
print(end.path_risk)

vertices.clear()

def add_risk(vals, x):
	result = []
	for val in vals:
		for _ in range(x):
			val += 1
			if val == 10: val = 1
		result.append(val)
	return result

def extend_risks(risks):
	global width, height
	
	for row in risks:
		row += add_risk(row, 1) + add_risk(row, 2) + add_risk(row, 3) + add_risk(row, 4)
	width *= 5
	new_risks = []
	for i in range(5):
		for row in risks:
			new_risks.append(add_risk(row, i))
	height *= 5
	return new_risks

risks = extend_risks(risks)

start = Vertex.at(0, 0)
start.path_risk = 0
score_paths(start)

end = Vertex.at(height - 1, width - 1)
print(end.path_risk)