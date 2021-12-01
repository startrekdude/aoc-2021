from sys import argv as args

path = args[1] if len(args) >= 2 else "sample-input.txt"
with open(path) as f:
	lines = f.read().splitlines()

data = [int(line) for line in lines]

increases = 0
for i in range(len(data) - 1):
	if data[i + 1] > data[i]:
		increases += 1
print(increases)

increases = 0
for i in range(len(data) - 3):
	s1 = sum(data[i:i+3])
	s2 = sum(data[i+1:i+4])
	if s2 > s1:
		increases += 1
print(increases)