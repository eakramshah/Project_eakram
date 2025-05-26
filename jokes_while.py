import random
import pyttsx3 

engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Set speaking speed

jokes = [
    "Why don’t scientists trust atoms? Because they make up everything!",
    "Why did the computer go to art school? Because it had a lot of bytes!",
    "What do you call a bear with no teeth? A gummy bear!",
    "Why was the math book sad? Because it had too many problems.",
    "Why did the robot go on vacation? Because it needed to recharge!"
]

print ("Welcome to Jokes counter !! Wanna Hear a Joke? Yes/No")
answer = input().strip().lower()
if answer == "yes":
    print ("Joke of the day")
    while True:
        joke = random.choice(jokes)
        print (joke)
        engine.say(joke)
        engine.runAndWait()

        print("Want to hear another joke !! Yes/No")
        again =input().strip().lower()
        if again != "yes":
           engine.say("Sure")
           engine.runAndWait()
           break
else:
 print( "See you! Maybe next time.")
engine.say("See you! Maybe next time.")
engine.runAndWait()
           
