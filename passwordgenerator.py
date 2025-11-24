import random
# Lowercase letters
nr_letters_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
# Uppercase lettersnr
nr_letters_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
# Numbers
nr_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Symbols
nr_symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
           '-', '_', '=', '+', '[', ']', '{', '}', ';', ':',
           "'", '"', ',', '<', '.', '>', '/', '?', '\\', '|']
print ("please help us how many letters and symbols you need to use for password\n")

lower_letter = int( input (" Give count for Lowerletter\n"))
upper_letter = int (input("Give count for UpperLetter\n"))
numbers_input = int (input ("how many numbers \n"))

# print ("Your password will be" + lower_letter_count+upper_letter_count+numbers_count)
passwordlist =[]
for char in range(0,lower_letter):
    passwordlist+=random.choice(nr_letters_lower)

for char in range(0,upper_letter):
    passwordlist+=random.choice(nr_letters_upper)

for char in range(0,numbers_input):
    passwordlist+=random.choice(nr_symbols)    
print (passwordlist)

print(random.shuffle(passwordlist))

print (passwordlist)

password=""
for char in passwordlist:
    password+=char
print ("Your password=", password)