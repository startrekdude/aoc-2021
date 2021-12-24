from sys import argv as args

path = args[1] if len(args) >= 2 else "input.txt"
with open(path) as f:
	lines = f.read().splitlines()

num = args[2] if len(args) >= 3 else "99999999999999"

registers = { "x": 0, "y": 0, "z": 0, "w": 0 }

def rsrc(src):
	if src.replace("-", "").isdigit(): return int(src)
	return registers[src]

for line in lines:
	opcode, *args = line.split(" ")
	if opcode == "inp":
		registers[args[0]] = int(num[0])
		num = num[1:]
	elif opcode == "add":
		registers[args[0]] += rsrc(args[1])
	elif opcode == "mul":
		registers[args[0]] *= rsrc(args[1])
	elif opcode == "div":
		registers[args[0]] //= rsrc(args[1])
	elif opcode == "mod":
		registers[args[0]] %= rsrc(args[1])
	elif opcode == "eql":
		registers[args[0]] = (registers[args[0]] == rsrc(args[1]))

print(registers["z"])