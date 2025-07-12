import random 
from random import randint 

EASY_LEVEL_TURN=5
HARD_LEVEL_TURN=10

def check_answer (user_guess,actual_answer):
    if user_guess > actual_answer:
        print ("Too high !! ")
    elif user_guess < actual_answer:
        print ("Too low")    
    else:
        print ( f"you got it !! {actual_answer}")    

def set_difficulty():
    level = input ("Choose Dificulty level ! 'easy' or 'hard' ")
    if level == "easy":
        turns= EASY_LEVEL_TURN
    else:
        turns = HARD_LEVEL_TURN

print ("welcome to the guessing number game \n ")

print ("Let computer guess a number between 1 and 100")

answer = randint(1,100)

guess=  input(int("Make a Guess !! "))