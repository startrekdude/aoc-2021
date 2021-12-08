from itertools import permutations
from sys import argv as args

path = args[1] if len(args) >= 2 else "sample-input.txt"
with open(path) as f:
	lines = f.read().splitlines()

result = 0
for line in lines:
	key, target = line.split(" | ")
	targets = target.split(" ")
	result += sum(1 for x in targets if len(x) == 2)
	result += sum(1 for x in targets if len(x) == 4)
	result += sum(1 for x in targets if len(x) == 3)
	result += sum(1 for x in targets if len(x) == 7)
print(result)

DIGITS = (
	frozenset("ABCEFG"),
	frozenset("CF"),
	frozenset("ACDEG"),
	frozenset("ACDFG"),
	frozenset("BCDF"),
	frozenset("ABDFG"),
	frozenset("ABDEFG"),
	frozenset("ACF"),
	frozenset("ABCDEFG"),
	frozenset("ABCDFG"),
)

REFERENCE = tuple("ABCDEFG")

def backmap(segments, p):
	result = set()
	for segment in segments:
		result.add(REFERENCE[p.index(segment)])
	return result

def solve_permutation(displays):
	for p in permutations(REFERENCE):
		if all(backmap(segments, p) in DIGITS for segments in displays):
			return p

result = 0
for line in lines:
	displays, target = line.split(" | ")
	displays = displays.split(" ")
	displays = [segments.upper() for segments in displays]
	p = solve_permutation(displays)
	
	target = target.split(" ")
	target = [segments.upper() for segments in target]
	digits = [DIGITS.index(backmap(segments, p)) for segments in target]
	n = int("".join(str(x) for x in digits))
	result += n

print(result)