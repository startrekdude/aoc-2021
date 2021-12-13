from dataclasses import dataclass
from sys import argv as args

path = args[1] if len(args) >= 2 else "sample-input.txt"
with open(path) as f:
	lines = f.read().splitlines()

@dataclass(frozen=True)
class Point:
	x : int
	y : int

@dataclass(frozen=True)
class Fold:
	axis : str
	pos  : int

holes = set()
folds = []

it = iter(lines)
while (line := next(it)):
	x, y = [int(s) for s in line.split(",")]
	holes.add(Point(x, y))

for line in it:
	line = line[len("fold along "):]
	axis, val = line.split("=")
	assert axis in {'x', 'y'}
	val = int(val)
	folds.append(Fold(axis, val))

def viz(holes):
	max_x = max(p.x for p in holes)
	max_y = max(p.y for p in holes)
	
	for y in range(max_y + 1):
		for x in range(max_x + 1):
			if Point(x, y) in holes:
				print("#", end="")
			else: print(".", end="")
		print()

def fold(holes, fold):
	def prop(p):
		if fold.axis == 'x': return p.x
		elif fold.axis == 'y': return p.y
	def sprop(p, z):
		if fold.axis == 'x':
			return Point(z, p.y)
		elif fold.axis == 'y':
			return Point(p.x, z)
	def fold_single(p):
		if prop(p) < fold.pos:
			return p
		delta = prop(p) - fold.pos
		return sprop(p, fold.pos - delta)
	
	result = set()
	for p in holes:
		result.add(fold_single(p))
	
	return result

holes = fold(holes, folds[0])

print(len(holes))

for f in folds[1:]:
	holes = fold(holes, f)

viz(holes)