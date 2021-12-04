from dataclasses import dataclass
from sys import argv as args

from copy import deepcopy

@dataclass
class Cell:
	val  : int
	mark : bool = False

# modify the file to end with two empty lines
path = args[1] if len(args) >= 2 else "sample-input.txt"
with open(path) as f:
	lines = f.read().splitlines()

def rmdups(s):
	while "  " in s:
		s = s.replace("  ", " ")
	return s

def read_board(it):
	board = []
	while (line := next(it)):
		board.append([Cell(int(x)) for x in rmdups(line).strip().split(" ")])
	return board

calls = [int(x) for x in lines[0].split(",")]
boards = []

it = iter(lines[2:])
try:
	while 1: boards.append(read_board(it))
except StopIteration: pass

def wins(board):
	for ri in range(5):
		if all(cell.mark for cell in board[ri]):
			return True
	for ci in range(5):
		if all(board[ri][ci].mark for ri in range(5)):
			return True

def calls_until_win(calls, boards):
	for call in calls:
		for board in boards:
			for ri in range(5):
				for ci in range(5):
					if board[ri][ci].val == call:
						board[ri][ci].mark = True
		for board in boards:
			if wins(board):
				return call, board

def calls_until_last_win(calls, boards):
	for call in calls:
		for board in boards:
			for ri in range(5):
				for ci in range(5):
					if board[ri][ci].val == call:
						board[ri][ci].mark = True
		
		if len(boards) == 1 and wins(boards[0]):
			return call, boards[0]
		
		for i in range(len(boards) - 1, -1, -1):
			if wins(boards[i]):
				del boards[i]

def sum_unmarked(board):
	result = 0
	for row in board:
		for cell in row:
			if not cell.mark:
				result += cell.val
	return result

last_call, winning_board = calls_until_win(calls, deepcopy(boards))
print(sum_unmarked(winning_board) * last_call)

last_call, winning_board = calls_until_last_win(calls, deepcopy(boards))
print(sum_unmarked(winning_board) * last_call)