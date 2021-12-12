from collections import defaultdict
from copy import copy
from sys import argv as args

path = args[1] if len(args) >= 2 else "sample-input.txt"
with open(path) as f:
	lines = f.read().splitlines()

vertices = set()
adjacent = defaultdict(set)

for line in lines:
	src, tgt = line.split("-")
	vertices.add(src)
	vertices.add(tgt)
	adjacent[src].add(tgt)
	adjacent[tgt].add(src)

def paths(prefix, visited):
	cur = prefix[-1]
	for vertex in adjacent[cur]:
		if vertex == "end":
			yield copy(prefix) + ["end"]
		elif vertex.isupper() or vertex not in visited:
			yield from paths(copy(prefix) + [vertex], copy(visited) | {vertex})

def paths2(prefix, visited, any_visited_twice):
	twice = any_visited_twice
	
	def can_visit(vertex):
		nonlocal twice
		twice = any_visited_twice
		
		if vertex.isupper():
			return True
		elif vertex == "start":
			return False
		elif vertex not in visited:
			return True
		elif vertex in visited and any_visited_twice == False:
			twice = True
			return True
		else:
			return False
	
	cur = prefix[-1]
	for vertex in adjacent[cur]:
		if vertex == "end":
			yield copy(prefix) + ["end"]
		elif can_visit(vertex):
			yield from paths2(copy(prefix) + [vertex], copy(visited) | {vertex}, twice)

def pprint_paths(paths):
	for path in paths:
		print(",".join(path))

all_paths = list(paths(["start"], {"start"}))
print(len(all_paths))

all_paths = list(paths2(["start"], {"start"}, False))
print(len(all_paths))