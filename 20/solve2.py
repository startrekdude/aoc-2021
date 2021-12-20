from sys import argv as args

path = args[1] if len(args) >= 2 else "sample-input.txt"
with open(path) as f:
	lines = f.read().splitlines()

enhancement = lines[0]

matrix = lines[2:]

def viz():
	print("\n".join(line for line in matrix))

def enlarge():
	global matrix
	new_line = "." * (len(matrix[0]) + 2)
	for i in range(len(matrix)):
		matrix[i] = "." + matrix[i] + "."
	matrix.insert(0, new_line)
	matrix.append(new_line)

def get_or_zero(y, x):
	try:
		return matrix[y][x]
	except:
		return "."

def enhance():
	global matrix
	
	new_matrix = []
	
	for y in range(len(matrix)):
		line = ""
		for x in range(len(matrix[0])):
			ks = (
				get_or_zero(y - 1, x - 1) +
				get_or_zero(y - 1, x)     +
				get_or_zero(y - 1, x + 1) +
				get_or_zero(y, x - 1)     +
				get_or_zero(y, x)         +
				get_or_zero(y, x + 1)     +
				get_or_zero(y + 1, x - 1) +
				get_or_zero(y + 1, x)     +
				get_or_zero(y + 1, x + 1)
			)
			key = int(ks.replace(".", "0").replace("#", "1"), 2)
			line += enhancement[key]
		new_matrix.append(line)
	
	matrix = new_matrix

#viz()
enhance()
enhance()
print()
#viz()

print(sum(sum(1 for c in line if c == "#") for line in matrix))