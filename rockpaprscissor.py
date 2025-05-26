import random

hand = ["rock", "paper", "scissor"]

user_input = input("Type R/P/S: ").lower()

# Convert short input to full choice
if user_input == "r":
    user_choice = "rock"
    print("You chose Rock")
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""") 
elif user_input == "p":
     user_choice = "paper"
     print("You chose Paper")
     print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

elif user_input == "s":
    user_choice = "scissor"
    print("You chose Scissor")
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
else:
    print("Input Invalid")
    exit()

computer_choice = random.choice(hand)

print("You chose:", user_choice)
print("Computer chose:", computer_choice)

# Determine the winner
if user_choice == computer_choice:
    print("It is a Tie")
elif (
    (user_choice == "rock" and computer_choice == "scissor") or 
    (user_choice == "paper" and computer_choice == "rock") or 
    (user_choice == "scissor" and computer_choice == "paper")
):
    print("You Won!")
else:
    print("Computer Wins!")
