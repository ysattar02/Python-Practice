from termcolor import colored
import numpy as np
import os

grid = [
  # 0           -->              #6
  [" ", " ", " ", " ", " ", " ", " "], # 0
  [" ", " ", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", " ", " "], 
  [" ", " ", " ", " ", " ", " ", " "],
  [" ", " ", " ", " ", " ", " ", " "] # 5
]

#  *** Functions *** 

# Build a Display eunction 
def display():

  print(f"""
  ************************************
  *********   Connect 4  *************
  ************************************
        ----------------------
        | {grid[0][0]}| {grid[0][1]}| {grid[0][2]}| {grid[0][3]}| {grid[0][4]}| {grid[0][5]}| {grid[0][6]}|
        ----------------------
        | {grid[1][0]}| {grid[1][1]}| {grid[1][2]}| {grid[1][3]}| {grid[1][4]}| {grid[1][5]}| {grid[1][6]}|
        ----------------------
        | {grid[2][0]}| {grid[2][1]}| {grid[2][2]}| {grid[2][3]}| {grid[2][4]}| {grid[2][5]}| {grid[2][6]}|
        ----------------------
        | {grid[3][0]}| {grid[3][1]}| {grid[3][2]}| {grid[3][3]}| {grid[3][4]}| {grid[3][5]}| {grid[3][6]}|
        ----------------------
        | {grid[4][0]}| {grid[4][1]}| {grid[4][2]}| {grid[4][3]}| {grid[4][4]}| {grid[4][5]}| {grid[4][6]}|
        ----------------------
        | {grid[5][0]}| {grid[5][1]}| {grid[5][2]}| {grid[5][3]}| {grid[5][4]}| {grid[5][5]}| {grid[5][6]}|
        ----------------------
          0  1  2  3  4  5  6

""")

def checkDiagonals(player):
  np_grid = np.array(grid)

  diags = [np_grid[::-1,:].diagonal(i) for i in range(-3,4)]
  diags.extend(np_grid.diagonal(i) for i in range(3,-4,-1))

  test_grid = []

  for i in [n.tolist() for n in diags]:
    test_grid.append(i)

  for i in range(1, len(test_grid)-1):
    counter = 0
    for e in test_grid[i]:
      if e == player:
        counter += 1
      else:
        counter = 0

      if counter == 4:
        return True


def validColumn(col):
  '''
  Loops through a given column of our grid, returns coordinate to update if there is available space,
  else returns False.
  '''
  if grid[0][col] != " ":
    return "Full"

  for i in range(5, -1, -1):
    if grid[i][col] == " ":
      return i

def is_winner(player):
   # Horizontal checks out
  for x in range(len(grid)):
    for y in range(len(grid[0]) - 3):
      if grid[x][y] == player and grid[x][y+1] == player and grid[x][y+2] == player and grid[x][y+3] == player:
        return True
  
 # Vertical
  for y in range(len(grid[0]) - 1):
    for x in range(len(grid) - 3):
      if grid[x][y] == player and grid[x+1][y] == player and grid[x+2][y] == player and grid[x+3][y] == player:
        return True

  # # Diagonal Check (both)
  if checkDiagonals(player):
    return True

  return False

    
# *** Game Loop ***


 # Initial setup
player_1 = input("Enter player one name: ")
playerOne_symbol = colored('X', 'blue', attrs=['bold'])

while True:
  player_2 = input("Enter player two name: ")

  if player_2 != player_1:
    break
  else:
    print("That name is being used by player one!")

playerTwo_symbol = colored('O', 'yellow', attrs=['bold'])

# Initial display
display()

while True:

  
  # Player one turn: 
  
  while True:
    player_move = input(f" {player_1} Enter the column of your choice (0-6): ")
    col = ''
    if player_move.isdigit() and int(player_move) < 7:
      col = int(player_move)
      
    else:
      print("Please Enter an integer from 0 - 6! ")
    # Get empty row, using validColumn() function
    if col != '':
      if validColumn(col) != "Full":
        row = validColumn(col) 
        # Update grid to reflect player move.
        grid[row][col] = playerOne_symbol
        break

  os.system('clear')
  display()
  if is_winner(playerOne_symbol):
    print(f"{player_1} has won!")
    break
  else:
    # Player two turn:
    while True:
      player_move = input(f"{player_2} Enter the column of your choice (0-6): ")
      col = ''
      if player_move.isdigit() and int(player_move) < 7:
        col = int(player_move)
       
      else:
        print("Please Enter an integer from 0 - 6! ")
      # Get empty row, using validColumn() function
      if col != '':
        if validColumn(col) != "Full":
          row = validColumn(col) 
          # Update grid to reflect player move.
          grid[row][col] = playerTwo_symbol
          break
    os.system('clear')
    display()
    if is_winner(playerTwo_symbol):
      print(f"{player_2} has won!")
      break


  
  
     






