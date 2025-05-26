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

print ("Welcome to the Joke World wanna hear a Joke\n")
answer = input().strip().lower()

if answer == "yes":
  name = input ("\nWhat is you name\n")
  print ("Hi\n" + name + " Here is a joke for you.\n")
  joke = random.choice(jokes)
  print(joke)
  engine.say(joke)
  engine.runAndWait()
  print("\nWant to hear one more? (yes/no)")
  answer2 = input().strip().lower()
  if answer2 == "yes":
     print ("Hi\n"  + " Here is a joke for you.\n")
     joke = random.choice(jokes)
     print (joke)
     engine.say(joke)
     engine.runAndWait()

  elif  answer2=="no":
    print ("\nOk no problem ! Maybe Next time ")
    engine.say("\n Ok no problem ! Maybe Next time ")
    engine.runAndWait()
else:
    print("\nOkay! Come back for more jokes anytime!")
    engine.say("Okay! Come back for more jokes anytime!")
    engine.runAndWait()