from collections import defaultdict
from dataclasses import dataclass
from itertools import product
from sys import argv as args

path = args[1] if len(args) >= 2 else "sample-input.txt"
with open(path) as f:
	lines = f.read().splitlines()

@dataclass(frozen=True)
class RebootCommand:
	on : bool
	x  : slice
	y  : slice
	z  : slice

def parse_slice(r):
	_, a = r.split("=")
	start, stop = a.split("..")
	return slice(int(start), int(stop))

commands = []

for line in lines:
	verb, rest = line.split(" ")
	on = verb == "on"
	xr, yr, zr = rest.split(",")
	commands.append(RebootCommand(
		on,
		parse_slice(xr),
		parse_slice(yr),
		parse_slice(zr),
	))

cubes = defaultdict(lambda: False)

def small(r):
	return -50 <= r.start <= 50 and -50 <= r.stop <= 50

def to_range(r):
	return range(r.start, r.stop + 1)

def run_command(command):
	for x, y, z in product(to_range(command.x), to_range(command.y), to_range(command.z)):
		cubes[(x, y, z)] = command.on

for command in commands:
	if small(command.x) and small(command.y) and small(command.z):
		run_command(command)

print(sum(cubes.values()))

CUBE_TEMPLATE = """
# cube.obj
#
 
g cube
 
v  {x_min}  {y_min}  {z_min}
v  {x_min}  {y_min}  {z_max}
v  {x_min}  {y_max}  {z_min}
v  {x_min}  {y_max}  {z_max}
v  {x_max}  {y_min}  {z_min}
v  {x_max}  {y_min}  {z_max}
v  {x_max}  {y_max}  {z_min}
v  {x_max}  {y_max}  {z_max}

vn  0.0  0.0  1.0
vn  0.0  0.0 -1.0
vn  0.0  1.0  0.0
vn  0.0 -1.0  0.0
vn  1.0  0.0  0.0
vn -1.0  0.0  0.0
 
f  1//2  7//2  5//2
f  1//2  3//2  7//2 
f  1//6  4//6  3//6 
f  1//6  2//6  4//6 
f  3//3  8//3  7//3 
f  3//3  4//3  8//3 
f  5//5  7//5  8//5 
f  5//5  8//5  6//5 
f  1//4  5//4  6//4 
f  1//4  6//4  2//4 
f  2//1  6//1  8//1 
f  2//1  8//1  4//1 
""".strip()

import pymesh
import os

def make_cube(x, y, z):
	return CUBE_TEMPLATE.format(
		x_min=float(x.start),
		x_max=float(x.stop + 1),
		y_min=float(y.start),
		y_max=float(y.stop + 1),
		z_min=float(z.start),
		z_max=float(z.stop + 1)
	)

def cube_for_command(command):
	return make_cube(command.x, command.y, command.z)

def mesh_for_command(command):
	cube = cube_for_command(command)
	with open("temp.obj", "w") as f:
		f.write(cube)
	mesh = pymesh.load_mesh("temp.obj")
	os.remove("temp.obj")
	return mesh

mesh = mesh_for_command(commands[0])

for command in commands[1:]:
	cmd_mesh = mesh_for_command(command)
	if command.on:
		mesh = pymesh.boolean(mesh, cmd_mesh, "union")
	else:
		mesh = pymesh.boolean(mesh, cmd_mesh, "difference")

print(f"Answer should be around: {round(mesh.volume)}")
print("(like within 50 of it. Have fun.)")