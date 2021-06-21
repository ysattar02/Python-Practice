from states_data import states
import random
import os
import time
# Create a dictionary where we have states as keys and capitals as values. 



states_capitals = {}

all_states = []

for i in states:
  # Updates dictionary with state:capital items
  state = i['name']
  capital = i['capital']
  states_capitals[state] = capital
  # Updates all_states with just states names
  all_states.append(state)
 
# Functions

def display():
  print(f"*** Score: {points} Remaining: {remaining_questions} ***") 




while True:

  # Game loop
  random.shuffle(all_states)

  # Globals
  points = 0
  remaining_questions = 15


  for i in range(0,15):
    os.system('clear')
    display()

    print(f"What is the capital of {all_states[i]}")
    user_answer = input("Enter the answer: ")

    if user_answer.lower() == states_capitals[all_states[i]].lower(): 
      points += 1
      remaining_questions -= 1
      print("You got that right!")
      time.sleep(1.5)
    else:
      remaining_questions -= 1
      print("You got that wrong!")
      time.sleep(1.5)

  print(f"You answered {points} questions correctly out of 15")
  
  game_rerun = input("Do you want to continue playing: y/n : ").lower()
  if game_rerun == 'n':
    print("Thanks for playing! ")
    break
    

      




