from collections import Counter
from dataclasses import dataclass
from itertools import product
from sys import argv as args

path = args[1] if len(args) >= 2 else "sample-input.txt"
with open(path) as f:
	lines = f.read().splitlines()

player1_pos = int(lines[0].split(": ")[1]) - 1
player2_pos = int(lines[1].split(": ")[1]) - 1
player1_score = 0
player2_score = 0

board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ddice_value = 1
ddice_count = 0

def ddice():
	global ddice_count, ddice_value
	ddice_count += 1
	result = ddice_value
	ddice_value += 1
	if ddice_value == 101:
		ddice_value = 1
	return result

def play_round():
	global player1_pos, player1_score, player2_pos, player2_score

	move1 = ddice() + ddice() + ddice()
	player1_pos = (player1_pos + move1) % 10
	player1_score += board[player1_pos]
	
	if player1_score >= 1000:
		return
	move2 = ddice() + ddice() + ddice()
	player2_pos = (player2_pos + move2) % 10
	
	
	player2_score += board[player2_pos]

while True:
	play_round()
	if player1_score >= 1000 or player2_score >= 1000:
		losing_score = min(player1_score, player2_score)
		break

print(losing_score * ddice_count)

player1_pos = int(lines[0].split(": ")[1]) - 1
player2_pos = int(lines[1].split(": ")[1]) - 1

@dataclass(frozen=True)
class Player:
	pos   : int
	score : int

@dataclass(frozen=True)
class Game:
	TURN_P1 = 0
	TURN_P2 = 1
	
	player1 : Player
	player2 : Player
	turn    : int = 0 # 0 or 1
	
	@property
	def ended(self):
		return self.player1.score >= 21 or self.player2.score >= 21
	
	def with_roll(self, roll):
		p1 = self.player1
		p2 = self.player2
		
		if self.turn == Game.TURN_P1:
			new_pos = (p1.pos + roll) % 10
			p1 = Player(
				new_pos,
				p1.score + new_pos + 1
			)
		elif self.turn == Game.TURN_P2:
			new_pos = (p2.pos + roll) % 10
			p2 = Player(
				new_pos,
				p2.score + new_pos + 1
			)
		else: assert False
		
		return Game(p1, p2, (self.turn + 1) % 2)

progenitor = Game(
	Player(player1_pos, 0),
	Player(player2_pos, 0),
)
states = Counter((progenitor,))

def superposition(states):
	new_states = Counter()
	for state, count in states.items():
		for r1, r2, r3 in product((1, 2, 3), repeat=3):
			roll = r1 + r2 + r3
			new_states[state.with_roll(roll)] += count
	return new_states

p1_wins = 0
p2_wins = 0

while states:
	states = superposition(states)
	for state in list(states.keys()):
		if state.ended:
			if state.player1.score > state.player2.score:
				p1_wins += states[state]
			else:
				p2_wins += states[state]
			del states[state]

print(max(p1_wins, p2_wins))