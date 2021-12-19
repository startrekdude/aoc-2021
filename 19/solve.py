from dataclasses import dataclass, replace
from itertools import combinations, permutations, product
from sys import argv as args
from typing import Optional

path = args[1] if len(args) >= 2 else "sample-input.txt"
with open(path) as f:
	lines = f.read().splitlines()

@dataclass(frozen=True)
class Point:
	x : int
	y : int
	z : int
	
	def manhattan(self, u):
		return abs(self.x - u.x) + abs(self.y - u.y) + abs(self.z - u.z)

@dataclass(frozen=True)
class Scanner:
	points : tuple
	abspos : Optional[Point]
	
	def absolute_points(self):
		for u in self.points:
			yield Point(u.x + self.abspos.x, u.y + self.abspos.y, u.z + self.abspos.z)
	
	def rotations(self):
		for x, y, z in permutations("xyz"):
			for neg_x, neg_y, neg_z in product((-1, 1), repeat=3):
				new_points = []
				for u in self.points:
					v = Point(
						getattr(u, x) * neg_x,
						getattr(u, y) * neg_y,
						getattr(u, z) * neg_z
					)
					new_points.append(v)
				yield Scanner(tuple(new_points), None)

fixed    = []
scanners = []

curr_points = []
for line in lines:
	if not line:
		scanners.append(Scanner(tuple(curr_points), None))
		curr_points = []
	elif line.startswith("---"): continue
	else:
		curr_points.append(Point(*(int(x) for x in line.split(","))))

fixed.append(replace(scanners.pop(0), abspos=Point(0, 0, 0)))

def fix(scanner, partner):
	aps = set(partner.absolute_points())
	for u in aps:
		for v in scanner.points:
			# hypothesize that u and v are actually the same point
			guess = Point(u.x - v.x, u.y - v.y, u.z - v.z)
			# try and confirm a detection cube
			count = 0
			for p in scanner.points:
				p = Point(p.x + guess.x, p.y + guess.y, p.z + guess.z)
				if p in aps: count += 1
			if count >= 12:
				return guess

while scanners:
	for i in range(len(scanners) - 1, -1, -1):
		for partner in fixed:
			for rotation in scanners[i].rotations():
				if (pos := fix(rotation, partner)):
					del scanners[i]
					fixed.append(replace(rotation, abspos=pos))
					
					print(f"\r{len(fixed)}/{len(fixed) + len(scanners)}", end="")
					
					break
			else: continue
			break

all_points = set()
for scanner in fixed:
	for u in scanner.absolute_points():
		all_points.add(u)
print(f"\r       \r{len(all_points)}")

greatest = 0
for first, second in combinations(fixed, 2):
	if (val := first.abspos.manhattan(second.abspos)) > greatest:
		greatest = val
print(greatest)