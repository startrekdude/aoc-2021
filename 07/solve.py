from sys import argv as args

path = args[1] if len(args) >= 2 else "sample-input.txt"
with open(path) as f:
	lines = f.read().splitlines()

crabs = list(int(x) for x in lines[0].split(","))

def alignment_cost(x):
	result = 0
	for crab in crabs:
		result += abs(crab - x)
	return result

def new_alignment_cost(x):
	result = 0
	for crab in crabs:
		n = abs(x - crab)
		result += (n * (n + 1)) // 2
	return result

answer = min(range(min(crabs), max(crabs) + 1), key=alignment_cost)
print(alignment_cost(answer))	

answer = min(range(min(crabs), max(crabs) + 1), key=new_alignment_cost)
print(new_alignment_cost(answer))