import random
def display_board(board):
  # simple board representation
  
  print('   |   |')
  print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
  print('   |   |')
  print('-----------')
  print('   |   |')
  print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
  print('   |   |')
  print('-----------')
  print('   |   |')
  print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
  print('   |   |')

# taking player input marker in tuple form
def player_input():
  marker = ''

  while not (marker == 'X' or marker == 'O'):
    marker = input('Player 1: Do you want to be X or O? ').upper()

  if marker == 'X':
    return ('X', 'O')
  else:
    return ('O', 'X')
      
# assignning the marker to the board position
def place_marker(board, marker, position):
  board[position] = marker

# win check funtion
def win_check(board,mark):
    
  return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
  (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
  (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
  (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
  (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
  (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
  (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
  (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

# random seletion to choose first player
def choose_first():
  if random.randint(0, 1) == 0:
    return 'Player 2'
  else:
    return 'Player 1'

# to check if board position is available
def space_check(board, position):
    
  return board[position] == ' '

# to check whether board is full or not
def full_board_check(board):
  for i in range(1,10):
    # usinh funtion space_check defined already
    if space_check(board, i):
      return False
  return True

# asking player for the position
def player_choice(board, player):
  position = 0
  
  while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
    position = input(f'Choose your next position {player}: (1-9) ')
    if position.isdigit():
      position = int(position)
      
  return position

# function to ask if players want to play again
def replay():    
  result =  input('Do you want to play again? Enter y or n: ').lower() 
  # print(result)
  if result == 'y':
    return True
  else:
    return False

# the actual game play
print('Welcome to Tic Tac Toe!')

while True:
  # Reset the board
  theBoard = [' '] * 10
  player1_marker, player2_marker = player_input()
  turn = choose_first()
  print(turn + ' will go first.')
  
  play_game = input('Are you ready to play? Enter y or n.')
  
  if play_game.lower()[0] == 'y':
    game_on = True
  else:
    game_on = False

  while game_on:
    if turn == 'Player 1':
      # Player1's turn.
      
      display_board(theBoard)
      position = player_choice(theBoard, turn)
      place_marker(theBoard, player1_marker, position)

      if win_check(theBoard, player1_marker):
        display_board(theBoard)
        print(f'Congratulations! You have won the game! {turn} "{player1_marker.upper()}"')
        game_on = False
      else:
        if full_board_check(theBoard):
          display_board(theBoard)
          print('The game is a draw!')
          break
        else:
          turn = 'Player 2'

    else:
      # Player2's turn.
      
      display_board(theBoard)
      position = player_choice(theBoard, turn)
      place_marker(theBoard, player2_marker, position)

      if win_check(theBoard, player2_marker):
        display_board(theBoard)
        print(f'Congratulations! You have won the game! {turn} "{player2_marker.upper()}"')
        game_on = False
      else:
        if full_board_check(theBoard):
          display_board(theBoard)
          print('The game is a draw!')
          break
        else:
          turn = 'Player 1'

  if not replay():
    break