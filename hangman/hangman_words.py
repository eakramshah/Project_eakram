import random
from word_list import word_list
from stages import stages

lives =6

print ("Welcome to Hangman game !!\n")

print ("\n"'''888                                                           
888                                                           
888                                                           
88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  
888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b 
888  888.d888888888  888888  888888  888  888.d888888888  888 
888  888888  888888  888Y88b 888888  888  888888  888888  888 
888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888 
                             888                              
                        Y8b d88P                              
                         "Y88P"                ''')

chosen_word = random.choice(word_list).lower()  # Make everything lowercase
print("Computer has chosen a Word you need to guess it !! you have 6 lives ")

word_length = len(chosen_word)
correct_letters = []
game_over = False

# Initial display
placeholder = "_" * word_length
print(placeholder)

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print("You already guessed that letter.")
        continue

    if guess in chosen_word:
        correct_letters.append(guess)

    display = ""
    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)
    if guess not in chosen_word:
        lives-=1
        if lives==0:
            game_over=True

            print ("You Loose !!")

    if "_" not in display:
        game_over = True
        print("You won!")
    print (stages[lives])