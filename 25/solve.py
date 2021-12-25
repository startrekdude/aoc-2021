from itertools import product
from sys import argv as args

path = args[1] if len(args) >= 2 else "sample-input.txt"
with open(path) as f:
	lines = f.read().splitlines()

seafloor = [list(line) for line in lines]
height = len(seafloor)
width = len(seafloor[0])

def step_east(seafloor):
	new_seafloor = [list("." * width) for _ in range(height)]
	for y, x in product(range(height), range(width)):
		c = seafloor[y][x]
		if c == ".": continue
		if c == "v":
			new_seafloor[y][x] = "v"
			continue
		
		new_x = (x + 1) % width
		if seafloor[y][new_x] == ".":
			new_seafloor[y][new_x] = ">"
		else:
			new_seafloor[y][x] = ">"
	return new_seafloor

def step_south(seafloor):
	new_seafloor = [list("." * width) for _ in range(height)]
	for y, x in product(range(height), range(width)):
		c = seafloor[y][x]
		if c == ".": continue
		if c == ">":
			new_seafloor[y][x] = ">"
			continue
		
		new_y = (y + 1) % height
		if seafloor[new_y][x] == ".":
			new_seafloor[new_y][x] = "v"
		else:
			new_seafloor[y][x] = "v"
	return new_seafloor

def step(seafloor):
	return step_south(step_east(seafloor))

def viz(seafloor):
	for line in seafloor:
		print("".join(line))

step_count = 0
while True:
	step_count += 1
	new_seafloor = step(seafloor)
	if new_seafloor == seafloor:
		break
	seafloor = new_seafloor

print(step_count)