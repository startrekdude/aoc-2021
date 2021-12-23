from collections import defaultdict
from dataclasses import dataclass, field
from enum import Enum
from sys import argv as args

LOOKBACK_THRESHOLD = 2
SHOW_SOLUTION = True

def replace(tp, i, x):
	return tp[:i] + (x,) + tp[i + 1:]

class AmphipodType(Enum):
	AMBER  = 'A', 1
	BRONZE = 'B', 10
	COPPER = 'C', 100
	DESERT = 'D', 1000
	
	def __new__(cls, letter, movement_cost):
		entry = object.__new__(cls)
		entry._value_ = letter
		entry._movement_cost_ = movement_cost
		return entry
	
	@property
	def movement_cost(self):
		return self._movement_cost_

@dataclass
class Enviroment:
	edges      : dict
	never_stop : frozenset
	stacks     : dict
	stack_size : int
	hallways   : frozenset = field(init=False)
	
	def __post_init__(self):
		self.hallways = frozenset(k for k in self.edges if k.startswith("hallway"))
	
	def paths(self, pos, occupied):
		paths    = {}
		distance = 1
		queue    = [pos]
		
		while queue:
			next_queue = []
			
			for pos in queue:
				for next_pos in self.edges[pos]:
					if next_pos in occupied or next_pos in paths: continue
					
					paths[next_pos] = distance
					next_queue.append(next_pos)
			
			queue = next_queue
			distance += 1
		
		return tuple((k, v) for k, v in paths.items() if k not in self.never_stop)

@dataclass(frozen=True)
class State:
	env       : Enviroment = field(hash=False)
	cost      : int
	positions : tuple
	history   : tuple = ()
	
	@property
	def occupied(self):
		return frozenset(pos for pod, pos in self.positions)
	
	@property
	def complete(self):
		return self.num_complete == len(self.positions)
	
	@property
	def num_complete(self):
		return sum(self.stack_length(pod) for pod in AmphipodType)
	
	def stack_length(self, pod):
		result = 0
		for pos in self.env.stacks[pod]:
			if (pod, pos) in self.positions:
				result += 1
			else: break
		return result
	
	def step(self):
		for i in range(len(self.positions)):
			pod, pos  = self.positions[i]
			stack_len = self.stack_length(pod)
			
			if stack_len == self.env.stack_size:
				continue
			
			target_pos = self.env.stacks[pod][stack_len]
			paths      = self.env.paths(pos, self.occupied)
			done       = False
			
			distance   = next(
				(distance for new_pos, distance in paths if new_pos == target_pos),
				None
			)
			if distance:
				yield State(
					self.env,
					self.cost + pod.movement_cost * distance,
					replace(self.positions, i, (pod, target_pos)),
					self.history + (self.positions,)
				)
				continue
			
			if pos in self.env.hallways: continue
			
			for new_pos, distance in paths:
				if new_pos not in self.env.hallways: continue
				yield State(
					self.env,
					self.cost + pod.movement_cost * distance,
					replace(self.positions, i, (pod, new_pos)),
					self.history + (self.positions,)
				)

def organize_amphipods(progenitor):
	best_costs      = {progenitor.positions: 0}
	best_complete   = None
	max_complete    = 0
	states          = {progenitor}
	iter_count      = 0
	
	while states:
		next_states = set()
		
		for state in states:
			for new_state in state.step():
				if new_state.positions in best_costs and best_costs[new_state.positions] <= new_state.cost:
					continue
				
				if best_complete and new_state.cost >= best_complete.cost:
					continue
				
				if new_state.complete:
					if not best_complete or new_state.cost < best_complete.cost:
						best_complete = new_state
					continue
				
				if new_state.num_complete > max_complete:
					max_complete = new_state.num_complete
				
				if new_state.num_complete < max_complete - LOOKBACK_THRESHOLD:
					continue
				
				best_costs[new_state.positions] = new_state.cost
				next_states.add(new_state)
		
		states = next_states
		iter_count += 1
		
		print(f"\r{iter_count}: #{len(states)} states, {max_complete} placed, path found: {best_complete is not None}", end="")
	print()
	
	return best_complete

def viz(positions, stack_prefixes):
	charmap = defaultdict(
		lambda: ".",
		{pos: pod.value for pod, pos in positions}
	)
	
	print("#############")
	print("#", end="")
	for i in range(1, 12):
		print(charmap[f"hallway{i}"], end="")
	print("#")
	
	print("###", end="")
	print(charmap["topRoomA"] + "#", end="")
	print(charmap["topRoomB"] + "#", end="")
	print(charmap["topRoomC"] + "#", end="")
	print(charmap["topRoomD"] + "#", end="")
	print("##")
	
	for prefix in stack_prefixes:
		print("  #", end="")
		print(charmap[prefix + "RoomA"] + "#", end="")
		print(charmap[prefix + "RoomB"] + "#", end="")
		print(charmap[prefix + "RoomC"] + "#", end="")
		print(charmap[prefix + "RoomD"] + "#", end="")
		print("  ")
	
	print("  #########  ")

def viz_path(path, stack_prefixes):
	for positions in path:
		viz(positions, stack_prefixes)
		print()

def read_puzzle():
	path = args[1] if len(args) >= 2 else "sample-input.txt"
	with open(path) as f:
		lines = f.read().splitlines()
	
	return (
		(AmphipodType(lines[2][3]), "topRoomA"),
		(AmphipodType(lines[3][3]), "botRoomA"),
		(AmphipodType(lines[2][5]), "topRoomB"),
		(AmphipodType(lines[3][5]), "botRoomB"),
		(AmphipodType(lines[2][7]), "topRoomC"),
		(AmphipodType(lines[3][7]), "botRoomC"),
		(AmphipodType(lines[2][9]), "topRoomD"),
		(AmphipodType(lines[3][9]), "botRoomD"),
	)

def main():
	puzzle_positions = read_puzzle()
	
	never_stop = frozenset((
		"hallway3",
		"hallway5",
		"hallway7",
		"hallway9",
	))
	env = Enviroment({
		"hallway1" : {"hallway2"},
		"hallway2" : {"hallway1", "hallway3"},
		"hallway3" : {"hallway2", "topRoomA", "hallway4"},
		"hallway4" : {"hallway3", "hallway5"},
		"hallway5" : {"hallway4", "topRoomB", "hallway6"},
		"hallway6" : {"hallway5", "hallway7"},
		"hallway7" : {"hallway6", "topRoomC", "hallway8"},
		"hallway8" : {"hallway7", "hallway9"},
		"hallway9" : {"hallway8", "topRoomD", "hallway10"},
		"hallway10": {"hallway9", "hallway11"},
		"hallway11": {"hallway10"},
		"topRoomA" : {"hallway3", "botRoomA"},
		"topRoomB" : {"hallway5", "botRoomB"},
		"topRoomC" : {"hallway7", "botRoomC"},
		"topRoomD" : {"hallway9", "botRoomD"},
		"botRoomA" : {"topRoomA"},
		"botRoomB" : {"topRoomB"},
		"botRoomC" : {"topRoomC"},
		"botRoomD" : {"topRoomD"},
	}, never_stop, {
		AmphipodType.AMBER : ("botRoomA", "topRoomA"),
		AmphipodType.BRONZE: ("botRoomB", "topRoomB"),
		AmphipodType.COPPER: ("botRoomC", "topRoomC"),
		AmphipodType.DESERT: ("botRoomD", "topRoomD"),
	}, 2)
	state = State(env, 0, puzzle_positions)
	
	solution = organize_amphipods(state)
	print(solution.cost)
	if SHOW_SOLUTION:
		viz_path(solution.history, ("bot",))
	
	env = Enviroment({
		"hallway1" : {"hallway2"},
		"hallway2" : {"hallway1", "hallway3"},
		"hallway3" : {"hallway2", "topRoomA", "hallway4"},
		"hallway4" : {"hallway3", "hallway5"},
		"hallway5" : {"hallway4", "topRoomB", "hallway6"},
		"hallway6" : {"hallway5", "hallway7"},
		"hallway7" : {"hallway6", "topRoomC", "hallway8"},
		"hallway8" : {"hallway7", "hallway9"},
		"hallway9" : {"hallway8", "topRoomD", "hallway10"},
		"hallway10": {"hallway9", "hallway11"},
		"hallway11": {"hallway10"},
		"topRoomA" : {"hallway3", "mhiRoomA"},
		"topRoomB" : {"hallway5", "mhiRoomB"},
		"topRoomC" : {"hallway7", "mhiRoomC"},
		"topRoomD" : {"hallway9", "mhiRoomD"},
		"mhiRoomA" : {"topRoomA", "mloRoomA"},
		"mhiRoomB" : {"topRoomB", "mloRoomB"},
		"mhiRoomC" : {"topRoomC", "mloRoomC"},
		"mhiRoomD" : {"topRoomD", "mloRoomD"},
		"mloRoomA" : {"mhiRoomA", "botRoomA"},
		"mloRoomB" : {"mhiRoomB", "botRoomB"},
		"mloRoomC" : {"mhiRoomC", "botRoomC"},
		"mloRoomD" : {"mhiRoomD", "botRoomD"},
		"botRoomA" : {"mloRoomA"},
		"botRoomB" : {"mloRoomB"},
		"botRoomC" : {"mloRoomC"},
		"botRoomD" : {"mloRoomD"},
	}, never_stop, {
		AmphipodType.AMBER : ("botRoomA", "mloRoomA", "mhiRoomA", "topRoomA"),
		AmphipodType.BRONZE: ("botRoomB", "mloRoomB", "mhiRoomB", "topRoomB"),
		AmphipodType.COPPER: ("botRoomC", "mloRoomC", "mhiRoomC", "topRoomC"),
		AmphipodType.DESERT: ("botRoomD", "mloRoomD", "mhiRoomD", "topRoomD"),
	}, 4)
	state = State(env, 0, puzzle_positions + (
		(AmphipodType.DESERT, "mhiRoomA"),
		(AmphipodType.DESERT, "mloRoomA"),
		(AmphipodType.COPPER, "mhiRoomB"),
		(AmphipodType.BRONZE, "mloRoomB"),
		(AmphipodType.BRONZE, "mhiRoomC"),
		(AmphipodType.AMBER , "mloRoomC"),
		(AmphipodType.AMBER , "mhiRoomD"),
		(AmphipodType.COPPER, "mloRoomD"),
	))
	
	solution = organize_amphipods(state)
	print(solution.cost)
	if SHOW_SOLUTION:
		viz_path(solution.history, ("mhi", "mlo", "bot"))

if __name__ == "__main__":
	main()