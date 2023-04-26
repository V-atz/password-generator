#random password generator

import random

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
          'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                     'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=',
                 '[', ']', '{', '}', '|', '\\', ';', ':', '\'', '\"', ',', '.', '/', '<', '>', '?']

password = []

print("Welcome to password generator : ")
req_upper  = int(input("How many upper case alphabets are needed ?\n"))
req_lower = int(input("How many lower case alphabets are needed ?\n"))
req_num = int(input("How many numbers are needed ?\n"))
req_spec = int(input("How many special characters are needed ?\n"))

for char in range ( 1 , req_upper + 1 ) :
    #loop will move in range of 1 and entered number of req_letter input
    password.append(random.choice(uppercase_letters))

for char in range ( 1 , req_lower + 1 ) :
    password.append(random.choice(letter))

for char in range ( 1 , req_num + 1 ) :
    password.append(random.choice(numbers))

for char in range ( 1 , req_spec + 1 ) :
    password.append(random.choice(special_chars))

#print(password)
random.shuffle(password)
#print(password)

new_pass = ""
for char in password :
    new_pass += char

print(f"Your password is : {new_pass}")