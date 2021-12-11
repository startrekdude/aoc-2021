from copy import deepcopy
from itertools import product
from sys import argv as args

path = args[1] if len(args) >= 2 else "sample-input.txt"
with open(path) as f:
	lines = f.read().splitlines()

octopi = [[int(c) for c in line] for line in lines]
initial_octopi = deepcopy(octopi)

def neighbours(y, x):
	for dy in (-1, 0, 1):
		for dx in (-1, 0, 1):
			if dy == 0 and dx == 0: continue
			
			y_, x_ = y + dy, x + dx
			
			if 0 <= y_ < 10 and 0 <= x_ < 10:
				yield y_, x_

def step(octopi):
	flash_queue = []
	flashed = set()
	for y, x in product(range(10), repeat=2):
		octopi[y][x] += 1
		if octopi[y][x] > 9:
			flashed.add((y, x))
			flash_queue.append((y, x))
	
	while flash_queue:
		y, x = flash_queue.pop(0)
		
		for y_, x_ in neighbours(y, x):
			octopi[y_][x_] += 1
			if octopi[y_][x_] > 9 and (y_, x_) not in flashed:
				flashed.add((y_, x_))
				flash_queue.append((y_, x_))
	
	for y, x in flashed:
		octopi[y][x] = 0
	
	return len(flashed)

def pprint(octopi):
	for line in octopi:
		print("".join(str(x) for x in line))

total = 0
for _ in range(100):
	total += step(octopi)
print(total)

octopi = initial_octopi

i = 0
while 1:
	i += 1
	count = step(octopi)
	if count == 100: break
print(i)