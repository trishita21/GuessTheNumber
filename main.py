from art import logo
import random

easy_level = 10
hard_level = 5

def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level.lower() == "hard":
    return hard_level
  else:
    return easy_level

def check_answer(guess,number):
  if guess == number:
    print(f"You got it! The answer was {number}.")
    return 1
  elif guess > number:
    print("Too high.")
  else:
    print("Too low.")
  return 0

def game():
  print(logo)
  
  print("Welcome to the Number Guessing Game!!")
  #print("I am thinking of a number between 1 to 100.")
  
  number = random.randint(1,100)
  attempts = 0
  print(f"Pssst, the correct answer is {number}")
  
  attempts = set_difficulty()
  
  while attempts > 0:
    print(f"You have {attempts} attempts to guess the number.")
    guess = int(input("Make a guess: "))

    check = check_answer(guess=guess, number=number)
    if check == 0:
      attempts -= 1
      if attempts == 0:
        print("You've run out of guesses, you lose.")
      else:
        print("Guess again.")
    else:
      break
  
game()
