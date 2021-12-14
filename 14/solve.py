from collections import Counter
from sys import argv as args

path = args[1] if len(args) >= 2 else "sample-input.txt"
with open(path) as f:
	lines = f.read().splitlines()

template = lines[0]
rules = {}
for line in lines[2:]:
	pair, elem = line.split(" -> ")
	rules[pair] = elem

def polymerize(state):
	new_state = ""
	for i in range(len(state) - 1):
		pair = state[i:i+2]
		new_state += state[i]
		if pair in rules:
			new_state += rules[pair]
	new_state += state[-1]
	return new_state

state = template
for _ in range(10):
	state = polymerize(state)

elems = Counter(state)
by_rarity = elems.most_common()
print(by_rarity[0][1] - by_rarity[-1][1])

class Polymer:
	def __init__(self, template):
		self.first_pair = template[:2]
		self.last_pair = template[-2:]
		
		self.state = Counter()
		for i in range(len(template) - 1):
			self.state[template[i:i+2]] += 1
	
	def polymerize(self):
		if self.first_pair in rules:
			self.first_pair = self.first_pair[0] + rules[self.first_pair]
		if self.last_pair in rules:
			self.last_pair = rules[self.last_pair] + self.last_pair[1]
		
		new_state = Counter()
		for pair, count in self.state.items():
			elem = rules[pair]
			new_pairs = (
				pair[0] + elem,
				elem + pair[1],
			)
			for new_pair in new_pairs:
				new_state[new_pair] += count
		self.state = new_state
	
	def elements(self):
		elems = Counter()
		elems[self.first_pair[0]] += 1
		elems[ self.last_pair[1]] += 1
		
		for pair, count in self.state.items():
			elems[pair[0]] += count
			elems[pair[1]] += count
		
		for pair in elems:
			elems[pair] //= 2
		
		return elems

state = Polymer(template)
for _ in range(40):
	state.polymerize()
elems = state.elements()
by_rarity = elems.most_common()
print(by_rarity[0][1] - by_rarity[-1][1])