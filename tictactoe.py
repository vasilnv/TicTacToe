import itertools

#prints all rows on new lines
'''for row in game:
	print(count, row)
	count += 1
'''

#check if it is a list
#print(type(game))

#prints them on 1 line
#print(game)

def game_board(game_map, player=0, row=0, column=0):
	try:
		if game_map[row][column] != 0:
			s = "   " + "  ".join([str[i] for i in range(len(game_map))])
			print(s)
			return game_map, False
		if player != 0:
			game_map[row][column]=player
			print("   0  1  2")
			for count, row in enumerate(game_map):
				print(count, row)
			return game_map, True
		else:
			return game_map
	except IndexError as e:
		print("Error: make sure you input row/column as 0, 1 or 2")
		return game_map, False
	except Exception as e:
		print("Something went very wrong!", e)
		return game_map, False

def win(current_board):
	def all_same(l):
		if l.count(l[0]) == len(l) and l[0] != 0:
			return True
		else:
			return False

	for row in current_board:
#		print (row)
		if all_same(row):
			print(f"player {row[0]} is the winner horizontally")
			return True

	for col in range(len(current_board)):
		check=[]
		
		for row in current_board:
			check.append(row[col])
		
		if all_same(check):
			print(f"player {check[0]} is the winner vertically")
			return True

	diags=[]
	for ix in range(len(game)):
		diags.append(current_board[ix][ix])
	if all_same(diags):
		print(f"player {diags[0]} is the winner (\\)")
		return True

	diags=[]
	cols = reversed(range(len(game)))
	rows = range(len(game))
	for col, row in zip(cols, rows):
		diags.append(game[row][col])
#	print(diags)
	if all_same(diags):
		print(f"player {diags[0]} is the winner (/)")
		return True
	return False

def endGame():
	game_won=True
	again=input("Over, do you want to play again?(y/n)")
	toplay=True
	if again.lower() == 'y':
		print("restartiiing")
	elif again.lower() == 'n':
		print ("byeee")
		toplay = False 
	else:
		print("not a valid answer")
		toplay = False
	return game_won, play

play = True
players=[1,2]
y = itertools.cycle(players)
while play:
	game=[[0, 0, 0],
		  [0, 0, 0],
	  	  [0, 0, 0]]
	print("here")
	game_won = False
	cnt=0
	while not game_won:
		current_player = next(y)
		played=False
		while not played:
			column_choice = int(input("What column do you want to play?: "))
			row_choice = int(input("What row do you want to play?: "))
			game, played = game_board(game, current_player, row_choice, column_choice)
			if(played):
				cnt=cnt+1

		if(win(game)):
			game_won=True
			again=input("Over, do you want to play again?(y/n)")
			if again.lower() == 'y':
				print("restartiiing")
			elif again.lower() == 'n':
				print ("byeee")
				play = False 
			else:
				print("not a valid answer")
				play = False
		if(cnt == 9):
			game_won, play = endGame()
'''	
	if current_board[0][0] == current_board[1][1] == current_board[2][2]:
		print("winner")
	elif current_board[0][2] == current_board[1][1] == current_board[2][0]:
		print("winner")
'''
