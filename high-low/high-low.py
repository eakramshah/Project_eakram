from util import logo, vs, data
import random

def main():


    print(logo)

    a= random.choice(data)
    b= random.choice(data)
    while a==b:
        b = random.choice(data)
    print (f"A:{a['name']} - A {a['description']} - From {a['country']} - Follower_count ?")
    print (vs)
    print (f"B:{b['name']} - A {b['description']} - From {b['country']} - Follower_count ?")
    guess_high_low = input("Who has more number of followers !! ? Type A: or B:").lower()
#Logic
    if a['follower_count'] > b['follower_count'] and guess_high_low == 'a':
        print(f"Correct! {a['name']} Has more Followers than {b['name']} ")
    elif b['follower_count'] > a["follower_count"] and guess_high_low =='b':
        print(f"Correct! {b['name']} Has more Followers than {a['name']} ")
    else:
        print("Wrong")    
    play_again =input ("Doyou want to play again ! Type: Y or N:").lower() 
    if play_again == "y":
        main()
    else:
        print (" Thankyou !")    
main()