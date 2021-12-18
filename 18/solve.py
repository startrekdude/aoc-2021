import re

from itertools import permutations
from math import floor, ceil
from sys import argv as args

path = args[1] if len(args) >= 2 else "sample-input.txt"
with open(path) as f:
	lines = f.read().splitlines()

def do_add(x, y):
	return f"[{x},{y}]"

LAST_NUM = re.compile(r"^(.*[^\d])(\d+)(.*?)$")
FIRST_NUM = re.compile(r"^(.*?)(\d+)(.*)$")
FIRST_NUM_TWO_DIGIT = re.compile(r"^(.*?[^\d])(\d{2,})(.*)$")
SIMPLE_PAIR = re.compile("^(.*)(\[\d+,\d+\])(.*)$")

def try_split(x):
	match = FIRST_NUM_TWO_DIGIT.match(x)
	if not match:
		return False, x
	
	prefix, target, suffix = match.group(1, 2, 3)
	target = int(target)
	first, second = floor(target / 2), ceil(target / 2)
	target = f"[{first},{second}]"
	
	return True, prefix + target + suffix

def try_explode(x):
	prefix = ""
	target = ""
	suffix = ""
	
	depth = 0
	it = iter(x)
	for c in it:
		if c == "[" and depth == 4:
			target += "["
			for c in it:
				target += c
				if c == "]": break
			for c in it:
				suffix += c
			break
		elif c == "[":
			depth += 1
		elif c == "]":
			depth -= 1
		prefix += c
	
	if prefix == x:
		return False, x
	
	first_num, second_num = (int(x) for x in target[1:-1].split(","))
	
	match = LAST_NUM.match(prefix)
	if match:
		_1, num, _3 = match.group(1, 2, 3)
		num = str(int(num) + first_num)
		prefix = _1 + num + _3
	
	match = FIRST_NUM.match(suffix)
	if match:
		_1, num, _3 = match.group(1, 2, 3)
		num = str(int(num) + second_num)
		suffix = _1 + num + _3
	
	return True, prefix + "0" + suffix

def do_reduce(x):
	while True:
		#print(x)
		did_change, x = try_explode(x)
		if did_change: continue
		did_change, x = try_split(x)
		if did_change: continue
		break
	return x

def do_magnitude(x):
	while not x.isdigit():
		match = SIMPLE_PAIR.match(x)
		prefix, target, suffix = match.group(1, 2, 3)
		first, second = (int(x) for x in target[1:-1].split(","))
		target = str(first * 3 + second * 2)
		x = prefix + target + suffix
	return int(x)

acc = lines[0]
for line in lines[1:]:
	acc = do_reduce(do_add(acc, line))

print(do_magnitude(acc))

highest = -999

for first, second in permutations(lines, 2):
	result = do_magnitude(do_reduce(do_add(first, second)))
	if result > highest:
		highest = result

print(highest)