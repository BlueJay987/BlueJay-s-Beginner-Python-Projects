#PASSWORD GENERATOR
import string
import random

#variables
characters = string.ascii_letters + string.digits + string.punctuation
pass_len = int(input("Input length of password: "))
pass_rep = int(input("Input # of passwords to generate: "))
output = ""

list(characters)
for j in range(pass_rep):
    output = ""
    for i in range(pass_len):
        symbol = random.choice(characters)
        output = output + symbol
    print("")
    print(output)        