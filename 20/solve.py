from collections import defaultdict
from itertools import product
from sys import argv as args

path = args[1] if len(args) >= 2 else "sample-input.txt"
with open(path) as f:
	lines = f.read().splitlines()

def is_lit(c):
	return c == "#"

enhancements = tuple(is_lit(c) for c in lines[0])

lines = lines[2:]

x_min = 0
x_max = len(lines[0])
y_min = 0
y_max = len(lines)

image = defaultdict(lambda: False)

for y, line in enumerate(lines):
	for x, c in enumerate(line):
		image[(y,x)] = is_lit(c)

def viz():
	for y in range(y_min, y_max):
		for x in range(x_min, x_max):
			print("#" if image[(y,x)] else ".", end="")
		print()

def keystring(y, x):
	result = (
		image[(y - 1, x - 1)] << 8 |
		image[(y - 1, x)]     << 7 |
		image[(y - 1, x + 1)] << 6 |
		image[(y, x - 1)]     << 5 |
		image[(y, x)]         << 4 |
		image[(y, x + 1)]     << 3 |
		image[(y + 1, x - 1)] << 2 |
		image[(y + 1, x)]     << 1 |
		image[(y + 1, x + 1)]
	)
	return result

def enhance(blanks_will_be=False):
	global image, x_min, x_max, y_min, y_max
	
	new_image = defaultdict(lambda: blanks_will_be)
	x_min -= 1
	x_max += 1
	y_min -= 1
	y_max += 1
	
	for y, x in product(range(y_min, y_max), range(x_min, x_max)):
		ks = keystring(y, x)
		new_image[(y, x)] = enhancements[ks]
	
	image = new_image

enhance(blanks_will_be=True)
enhance(blanks_will_be=False)
viz()

print(sum(1 for x in image.values() if x))

x_min = 0
x_max = len(lines[0])
y_min = 0
y_max = len(lines)

image = defaultdict(lambda: False)

for y, line in enumerate(lines):
	for x, c in enumerate(line):
		image[(y,x)] = is_lit(c)

alternate_blanks = True
for _ in range(50):
	enhance(blanks_will_be=alternate_blanks)
	alternate_blanks = not alternate_blanks

print(sum(image.values()))