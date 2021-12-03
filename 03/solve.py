from sys import argv as args

path = args[1] if len(args) >= 2 else "sample-input.txt"
with open(path) as f:
	lines = f.read().splitlines()

gamma_rate = ""
epsilon_rate = ""

most_common = {}

for i in range(len(lines[0])):
	zeros = 0
	ones = 0
	for line in lines:
		if line[i] == "0":
			zeros += 1
		elif line[i] == "1":
			ones += 1
		else:
			assert False
	if zeros > ones:
		gamma_rate += "0"
		epsilon_rate += "1"
		most_common[i] = "0"
	else:
		gamma_rate += "1"
		epsilon_rate += "0"
		most_common[i] = "1"
	
	if zeros == ones:
		most_common[i] = "EQ"

gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)
print(gamma_rate * epsilon_rate)

ox_candidates = lines.copy()
co_candidates = lines.copy()

def cbp(a, i):
	zeros = 0
	ones = 0
	for x in a:
		if x[i] == "0":
			zeros += 1
		elif x[i] == "1":
			ones += 1
	if zeros > ones:
		return "0"
	elif ones > zeros:
		return "1"
	else:
		return "EQ"

i = 0
while len(ox_candidates) > 1 or len(co_candidates) > 1:
	key_ox = cbp(ox_candidates, i)
	if len(ox_candidates) > 1:
		for j in range(len(ox_candidates) - 1, -1, -1):
			if (ox_candidates[j][i] != key_ox):
				if not key_ox == "EQ" or ox_candidates[j][i] != "1":
					del ox_candidates[j]
	key_co = cbp(co_candidates, i)
	if len(co_candidates) > 1:
		for j in range(len(co_candidates) - 1, -1, -1):
			if (co_candidates[j][i] == key_co) or (key_co == "EQ" and co_candidates[j][i] == "1"):
				del co_candidates[j]
	i += 1

ox = int(ox_candidates[0], 2)
co = int(co_candidates[0], 2)

print(ox * co)