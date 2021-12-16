from byref import byref
from dataclasses import dataclass
from functools import reduce
from io import StringIO
from operator import mul
from sys import argv as args

path = args[1] if len(args) >= 2 else "sample-input.txt"
with open(path) as f:
	lines = f.read().splitlines()

@dataclass(frozen=True)
class Node:
	version : int
	type_id : int
	value   : int
	children: tuple

data = "{:b}".format(int(lines[0], 16))
if len(data) % 2 != 0:
	data = "0" + data
f = StringIO(data)

@byref("length_read")
def read_literal(f, length_read, /):
	bits = ""
	while 1:
		datum = f.read(5)
		length_read += 5
		bits += datum[1:]
		if datum[0] == "0": break
	return int(bits, 2)

@byref("length_read")
def read_children(f, length_read, /):
	children = []
	length_type = int(f.read(1), 2)
	length_read += 1
	
	if length_type == 0:
		size = int(f.read(15), 2)
		length_read += 15
		
		sub_length_read = 0
		while sub_length_read < size:
			children.append(read_packet(f, sub_length_read))
		length_read += size
	else:
		num_packets = int(f.read(11), 2)
		length_read += 11
		for _ in range(num_packets):
			children.append(read_packet(f, length_read))
	
	return tuple(children)

@byref("length_read")
def read_packet(f, length_read, /):
	version  = int(f.read(3), 2)
	type_id  = int(f.read(3), 2)
	value    = -1
	children = ()
	length_read += 6
	
	if type_id == 4:
		value = read_literal(f, length_read)
	else:
		children = read_children(f, length_read)
	
	return Node(version, type_id, value, children)

def sum_versions(node):
	result = node.version
	for child in node.children:
		result += sum_versions(child)
	return result

length_read = 0
root = read_packet(f, length_read)
print(sum_versions(root))

def eval_node(node):
	children = (eval_node(u) for u in node.children)
	
	if   node.type_id == 4: # LITERAL
		return node.value
	elif node.type_id == 0: # SUM
		return sum(children)
	elif node.type_id == 1: # PRODUCT
		return reduce(mul, children, 1)
	elif node.type_id == 2: # MINIMUM
		return min(children)
	elif node.type_id == 3: # MAXIMUM
		return max(children)
	elif node.type_id == 5: # GREATER_THAN
		return int(next(children) > next(children))
	elif node.type_id == 6: # LESS THAN
		return int(next(children) < next(children))
	elif node.type_id == 7: # EQUAL
		return int(next(children) == next(children))
	else: assert False

print(eval_node(root))