from sys import argv as args

path = args[1] if len(args) >= 2 else "sample-input.txt"
with open(path) as f:
	lines = f.read().splitlines()

starting = ('(', '[', '{', '<')
ending   = (')', ']', '}', '>')

scores = {
	')': 3,
	']': 57,
	'}': 1197,
	'>': 25137,
}

scores2 = {
	')': 1,
	']': 2,
	'}': 3,
	'>': 4,
}

def first_corrupt(line):
	stack = []
	for c in line:
		if c in starting:
			stack.append(c)
		elif c in ending:
			expect = ending[starting.index(stack.pop())]
			if c != expect:
				return c
	return None

def autocomplete(line):
	stack = []
	for c in line:
		if c in starting:
			stack.append(c)
		elif c in ending:
			stack.pop()
	return "".join(reversed([ending[starting.index(c)] for c in stack]))

def score_ac(s):
	result = 0
	for c in s:
		result *= 5
		result += scores2[c]
	return result

result = 0

good_lines = []

for line in lines:
	c = first_corrupt(line)
	if c:
		result += scores[c]
	else: good_lines.append(line)

print(result)

lines = good_lines

scores = []
for line in lines:
	ac = autocomplete(line)
	score = score_ac(ac)
	scores.append(score)

scores.sort()

print(scores[len(scores) // 2])