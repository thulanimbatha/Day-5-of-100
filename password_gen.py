# Generate a password

import random
import string

# get alphabets - Uppercase & Lowercase
alphabet = string.ascii_letters
# put letters in list
alph_list = list(alphabet)
#  number list
num_list = list(str(range(0,10)))
#  symbol list
sym_list = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

'''PROGRAM START'''
print("\tWelcome to the Password Generator!\t")
num_letters = int(input("How many letters would you like in your password? "))
num_digits = int(input("How many digits would you like in your password? "))
num_symbols = int(input("How many symbols would you like in your password? "))

# password 
password = ""
'''EASY LEVEL'''
for char in range(1, num_letters + 1):
    password += random.choice(alph_list)
for sym in range(1, num_symbols + 1):
    password += random.choice(sym_list)
for num in range(1, num_digits + 1):
    password += random.choice(num_list)   
print(password, "\n")

'''HARD LEVEL'''
password_list = []
for char in range(1, num_letters + 1):
    password_list.append(random.choice(alph_list))
for sym in range(1, num_symbols + 1):
    password_list.append(random.choice(sym_list))
for num in range(1, num_digits + 1):
    password_list.append(random.choice(num_list))   

# now we need to shuffle the order of the contents of the list
random.shuffle(password_list)
print(password_list)

# turn it into a string
password2 = ""
for value in password_list:
    password2 += value
print(f"Your password is: {password2}")