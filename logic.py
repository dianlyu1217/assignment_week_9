import logging
import random
import csv

logger = logging.getLogger('tictactoe')


class Game:
	def __init__(self, single: bool):
		self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
		self.x = Human('X', self)
		if single:
			self.y = Robot('O', self)
		else:
			self.y = Human('O', self)
		self.turn = random.choice([self.x, self.y])
		if self.turn is self.x:
			self.first = self.x.get_name()
		else:
			self.first = self.y.get_name()
		self.show_board()
	
	def show_board(self):
		for row in self.board:
			print(row)
		print('---current board---')
	
	def change_turn(self):
		if self.turn is self.x:
			self.turn = self.y
		else:
			self.turn = self.x
	
	def judge_winner(self) -> bool:
		for i in range(0, 3):
			if self.board[i][0] != ' ' and self.board[i][0] == self.board[i][1] == self.board[i][2]:
				winner = self.board[i][0]
				logger.info('{turn} won'.format(turn=winner))
				print(winner, ' Won')
				self.collect_data(winner)
				return True
		for i in range(0, 3):
			if self.board[0][i] != ' ' and self.board[0][i] == self.board[1][i] == self.board[2][i]:
				winner = self.board[0][i]
				logger.info('{turn} won'.format(turn=winner))
				print(winner, ' Won')
				self.collect_data(winner)
				return True
		if self.board[1][1] != ' ' and (
				self.board[0][0] == self.board[1][1] == self.board[2][2] or self.board[2][0] == self.board[1][1] ==
				self.board[0][2]):
			winner = self.board[1][1]
			logger.info('{turn} won'.format(turn=winner))
			print(winner, ' Won')
			self.collect_data(winner)
			return True
		for row in self.board:
			for col in row:
				if col == ' ':
					return False
		logger.info('Draw')
		self.collect_data('Draw')
		print('Draw')
		return True
	
	def collect_data(self, result: str):
		path = "./database.csv"
		try:
			f = open(path)
			f.close()
		except IOError:
			with open(path, 'w') as f:
				w = csv.writer(f)
				h = ["Winner", "StepNumber", "FirstPlayer"]
				w.writerow(h)
		
		stepNum = 0
		for row in self.board:
			for col in row:
				if col != ' ':
					stepNum += 1
		
		with open(path, 'a') as f:
			w = csv.writer(f)
			h = [result, stepNum, self.first]
			w.writerow(h)


class Gamer:
	def __init__(self, name: str, game: Game):
		self.name = name
		self.game = game
	
	def get_name(self) -> str:
		return self.name


class Human(Gamer):
	def __init__(self, name: str, game: Game):
		super().__init__(name, game)
	
	def do_round(self):
		while True:
			r = input("[{turn} turn] input row index: ".format(turn=self.name))
			c = input("[{turn} turn] input col index: ".format(turn=self.name))
			if self.check_input(r, c):
				self.game.board[int(r)][int(c)] = self.name
				break
	
	def check_input(self, r: str, c: str) -> bool:
		if not r.isdigit() or not c.isdigit():
			logger.error('{turn} input invalid: {r},{c}'.format(turn=self.name, r=r, c=c))
			print('input invalid, not int')
			return False
		elif int(r) < 0 or int(r) > 2 or int(c) < 0 or int(c) > 2:
			logger.error('{turn} input invalid: {r},{c}'.format(turn=self.name, r=r, c=c))
			print('input invalid, should >=0 and <=2')
			return False
		elif self.game.board[int(r)][int(c)] != ' ':
			logger.error('{turn} input invalid: {r},{c}'.format(turn=self.name, r=r, c=c))
			print('input invalid, index already input')
			return False
		else:
			logger.info('received {turn} input: {r},{c}'.format(turn=self.name, r=r, c=c))
			return True


# def get_name(self) -> str:
# 	return self.name


class Robot(Gamer):
	def __init__(self, name: str, game: Game):
		super().__init__(name, game)
	
	def do_round(self):
		empty_coordinates = [(row, col) for row in range(3) for col in range(3) if self.game.board[row][col] == ' ']
		r, c = random.choice(empty_coordinates)
		logger.info('{turn} random input: {r},{c}'.format(turn=self.name, r=r, c=c))
		self.game.board[r][c] = self.name
		print('[{turn} turn] robot automatic input index: {r},{c}'.format(turn=self.name, r=r, c=c))

# def get_name(self) -> str:
# 	return self.name
