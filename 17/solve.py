# run this one with PyPy :)

from itertools import product
from sys import argv as args

path = args[1] if len(args) >= 2 else "sample-input.txt"
with open(path) as f:
	lines = f.read().splitlines()

line = lines[0][15:]
xrange, yrange = line.replace("y=", "").split(", ")
x_min, x_max = [int(x) for x in xrange.split("..")]
y_min, y_max = [int(x) for x in yrange.split("..")]

class Probe:
	def __init__(self, dx, dy):
		self.x = 0
		self.y = 0
		self.max_y = 0
		self.dx = dx
		self.dy = dy
	def step(self):
		self.x += self.dx
		self.y += self.dy
		self.max_y = max(self.max_y, self.y)
		if self.dx > 0:
			self.dx -= 1
		elif self.dx < 0:
			self.dx += 1
		self.dy -= 1
	def in_target_area(self):
		return (
			x_min <= self.x <= x_max and
			y_min <= self.y <= y_max
		)
	def below_target_area(self):
		return self.y < y_min

highest_y = -999
initials = set()

for dx, dy in product(range(-201, 301), repeat=2):
	probe = Probe(dx, dy)
	while not probe.below_target_area():
		probe.step()
		if probe.in_target_area():
			initials.add((dx, dy))
			if probe.max_y > highest_y:
				highest_y = probe.max_y
				result = dx, dy
			break

print(highest_y, result)
print(len(initials))