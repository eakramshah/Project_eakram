from logo import logo
from alphabet import alphabet
from mask import mask
print(logo)
def ceaser (original_text,shift_amount,encode_or_decode):
    cypher_text=""
    if encode_or_decode=="decode":
        shift_amount*= -1 
    for letter in original_text:
       shifted_position= alphabet.index(letter) + shift_amount
       shifted_position%=len(alphabet)
       cypher_text+= alphabet[ shifted_position ]
    print (f"here is the {encode_or_decode}d \n{cypher_text}")

should_continue = True
while should_continue:
    print (mask)
    direction = input('''Type  'encode' or 'decode' to Encrypt or Decypt code \n ''').lower()
    text = input("Type your message !! \n").lower()
    shift = int ( input ("You SECRET number : \n"))
    ceaser (original_text=text,shift_amount=shift,encode_or_decode=direction)
    restart = input("Type YES if you want to go again, otherwise NO. \n").lower()
    if restart=="no":
        should_continue=False
        print ("Will Exit now - Good bye !! ")
