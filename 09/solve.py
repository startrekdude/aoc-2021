from itertools import product
from sys import argv as args

path = args[1] if len(args) >= 2 else "sample-input.txt"
with open(path) as f:
	lines = f.read().splitlines()

env = [[int(x) for x in line] for line in lines]
width = len(env[0])
height = len(env)

low_points = set()

result = 0
for y, x in product(range(height), range(width)):
	adj = ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1))
	curr = env[y][x]
	lowest = True
	for a in adj:
		y_, x_ = a
		if 0 <= y_ < height:
			if 0 <= x_ < width:
				if env[y_][x_] <= curr:
					lowest = False
	if lowest:
		low_points.add((y, x))
		result += curr + 1

print(result)

basins = []

for lp in low_points:
	basin = [lp]
	queue = [lp]
	while queue:
		next_queue = []
		for y, x in queue:
			adj = ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1))
			curr = env[y][x]
			for a in adj:
				y_, x_ = a
				if 0 <= y_ < height and 0 <= x_ < width:
					if env[y_][x_] > curr and env[y_][x_] != 9:
						if (y_, x_) not in basin:
							basin.append((y_, x_))
							next_queue.append((y_, x_))
		queue = next_queue
	basins.append(basin)

basins = sorted(basins, key=len, reverse=True)

print(len(basins[0]) * len(basins[1]) * len(basins[2]))