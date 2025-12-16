from util import logo, vs, data
import random

def game():
    total_score = 0
    print(logo)

    while True:
        a = random.choice(data)
        b = random.choice(data)
        while a == b:
            b = random.choice(data)

        print(f"A: {a['name']} - {a['description']} - From {a['country']}")
        print(vs)
        print(f"B: {b['name']} - {b['description']} - From {b['country']}")

        guess = input("Who has more followers? Type A or B: ").lower()

        if a['follower_count'] > b['follower_count'] and guess == 'a':
            total_score += 1
            print(f"Correct! {a['name']} has more followers.")
        elif b['follower_count'] > a['follower_count'] and guess == 'b':
            total_score += 1
            print(f"Correct! {b['name']} has more followers.")
        else:
            print(f"Wrong! Final Score: {total_score}")
            break

        print(f"Current Score: {total_score}")
        play_again = input("Play again? Type Y or N: ").lower()
        if play_again != 'y':
            print(f"Thank you for playing! Final Score: {total_score}")
            break

game()
