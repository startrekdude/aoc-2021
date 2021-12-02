from sys import argv as args

path = args[1] if len(args) >= 2 else "sample-input.txt"
with open(path) as f:
	lines = f.read().splitlines()

x = 0
y = 0

for line in lines:
	command, arg = line.split(" ")
	arg = int(arg)
	if command == "forward":
		x += arg
	elif command == "down":
		y += arg
	elif command == "up":
		y -= arg
	else:
		assert False

print(x*y)

x = 0
y = 0
aim = 0

for line in lines:
	command, arg = line.split(" ")
	arg = int(arg)
	if command == "forward":
		x += arg
		y += arg * aim
	elif command == "down":
		aim += arg
	elif command == "up":
		aim -= arg
	else:
		assert False

print(x*y)