from random import randint

EASY_LEVEL_TURN = 5
HARD_LEVEL_TURN = 10


def check_answer(user_guess, actual_answer):
    if user_guess > actual_answer:
        print("Too high!")
        return False
    elif user_guess < actual_answer:
        print("Too low!")
        return False
    else:
        print(f"You got it!! {actual_answer}")
        return True


def set_difficulty():
    level = input("Choose Difficulty level! 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURN
    else:
        return HARD_LEVEL_TURN


def game():
    print("\nWelcome to the guessing number game")
    print("Let computer guess a number between 1 and 100")

    answer = randint(1, 100)
    turns = set_difficulty()

    while turns > 0:
        print(f"\nYou have {turns} attempts remaining!")
        guess = int(input("Make a Guess!! "))

        correct = check_answer(guess, answer)

        if correct:
            break

        turns -= 1

        if turns == 0:
            print(f"You lost! The answer was {answer}")

    # 🔁 RECURSION
    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again == "y":
        game()
    else:
        print("Thanks for playing!")


game()
