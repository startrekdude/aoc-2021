from collections import Counter
from copy import copy
from sys import argv as args

path = args[1] if len(args) >= 2 else "sample-input.txt"
with open(path) as f:
	lines = f.read().splitlines()

fish = Counter(int(x) for x in lines[0].split(","))

def sim(fish):
	result = Counter()
	for k, v in fish.items():
		if k == 0:
			result[6] += v
			result[8] += v
		else:
			result[k - 1] += v
	return result

ref = copy(fish)

for _ in range(80):
	fish = sim(fish)

# assert fish == Counter((6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8))

print(sum(fish.values()))

fish = ref

for _ in range(256):
	fish = sim(fish)

print(sum(fish.values()))