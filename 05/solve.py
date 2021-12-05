from collections import Counter
from dataclasses import dataclass
from sys import argv as args

path = args[1] if len(args) >= 2 else "sample-input.txt"
with open(path) as f:
	lines = f.read().splitlines()

@dataclass(frozen=True)
class Point:
	x : int
	y : int

def trunc(x):
	if x == 0:
		return x
	elif x < 0:
		return -1
	else:
		return 1

@dataclass(frozen=True)
class Line:
	start : Point
	end   : Point
	
	def follow(self, allow_diagonal=False):
		dx = trunc(self.end.x - self.start.x)
		dy = trunc(self.end.y - self.start.y)
		
		if not allow_diagonal and dx + dy not in (1, -1): return
		
		curr = self.start
		while curr != self.end:
			yield curr
			curr = Point(curr.x + dx, curr.y + dy)
		yield curr

def to_point(s):
	parts = s.split(",")
	return Point(int(parts[0]), int(parts[1]))

vents = [] # sussy baka ?

for line in lines:
	first, second = line.split(" -> ")
	vents.append(Line(to_point(first), to_point(second)))

seafloor = Counter()

for vent in vents:
	for pos in vent.follow():
		seafloor[pos] += 1

def count_overlaps(c):
	result = 0
	for k, i in c.items():
		if i >= 2:
			result += 1
	return result

print(count_overlaps(seafloor))

seafloor = Counter()

for vent in vents:
	for pos in vent.follow(allow_diagonal=True):
		seafloor[pos] += 1

print(count_overlaps(seafloor))