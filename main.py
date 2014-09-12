#The main python file

#initiate cars with their positions
board = []
	for i in range(6):
		for k in range(6):
			board[i][k] = '.'
printboard(board)
while True:
	#ask for user input
	move(board)
	printboard
	if win:
		print something
		break