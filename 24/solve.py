import subprocess

from os import chdir
from sys import argv as args

path = args[1] if len(args) >= 2 else "input.txt"
with open(path) as f:
	lines = f.read().splitlines()

curr_digit = 0

def next_digit():
	global curr_digit
	curr_digit += 1
	return f"digit{curr_digit}"

def literal(s):
	if s.replace("-", "").isdigit():
		return f"{s}ll";
	return s

def transpile(line):
	opcode, *args = line.split(" ")
	if   opcode == "inp":
		return f"{args[0]} = {next_digit()};"
	elif opcode == "add":
		return f"{args[0]} += {literal(args[1])};"
	elif opcode == "mul":
		return f"{args[0]} *= {literal(args[1])};"
	elif opcode == "div":
		return f"{args[0]} /= {literal(args[1])};"
	elif opcode == "eql":
		return f"{args[0]} = {args[0]} == {literal(args[1])};"
	elif opcode == "mod":
		x = args[0]
		m = literal(args[1])
		return f"{x} = ({x} % {m} + {m}) % {m};"
	else: assert False

def kernel(lines):
	result = [
		"static inline __attribute__((always_inline)) int64_t kernel(",
	]
	
	for i in range(1, 15):
		result.append(f"\t const uint8_t digit{i}{(i != 14) * ','}")
	
	result += [
		") {",
		"\tint64_t x = 0;",
		"\tint64_t y = 0;",
		"\tint64_t z = 0;",
		"\tint64_t w = 0;",
		"",
	]
	
	for line in lines:
		result.append(f"\t{transpile(line)}")
	
	result.append("\treturn z;")
	result.append("}")
	
	return "\n".join(result)

chdir("solver")

with open("kernel.c", "w") as f:
	f.write(kernel(lines))

def compile_worker(opt):
	subprocess.call([
		"gcc",
		"-osolver.exe",
		"solver.c",
		"-O3",
		"-march=native",
		opt,
	])

compile_worker("-DPART1")
subprocess.call(["solver"])

compile_worker("-DPART2")
subprocess.call(["solver"])