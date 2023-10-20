#Key Generator
import random
import string

chunk1 = "000"
placeholder = 1
letters = list(string.ascii_uppercase)

mode = input("Generate or Check?")
mode = mode.lower()

if mode == "check":
    usercode = input("Enter code: ")
    
    valid = True

    c1 = usercode[0] + usercode[1] + usercode[2]

    if c1 == "000":
        placeholder = 2
    elif c1 != "000":
        valid = False

    #chunk 2
    n1 = int(usercode[4])
    n2 = int(usercode[5])
    n3 = int(usercode[6])

    if n1 + n2 + n3 != 10:
        valid = False
    
    #chunk 3
    l1 = letters.index(usercode[8])
    l2 = letters.index(usercode[9])
    l3 = letters.index(usercode[10])
    if l1 + l2 + l3 > 30:
        valid = False

    #Chunk 4
    nn1 = int(usercode[12])
    nn2 = int(usercode[13])
    nn3 = int(usercode[14])
    nn4 = int(usercode[15])

    if nn1 - nn2 - nn3 - nn4 < 0:
        valid = False
    
    if valid == False:
        print("INVALID")
    elif valid == True:
        print("VALID")

elif mode == "generate":
    
    #c1 is already generated

    #Generate c2
    active = True
    while active:
        n1 = random.randint(0,9)
        n2 = random.randint(0,9)
        n3 = random.randint(0,9)
        if n1+n2+n3 == 10:
            chunk2 = str(n1)+str(n2)+str(n3)
            active = False

    #Generate c3
    active = True
    while active:
        l1 = random.randint(0,25)
        l2 = random.randint(0,25)
        l3 = random.randint(0,25)
        if l1 + l2 + l3 < 30:
            chunk3 = letters[l1] + letters[l2] + letters[l3]
            active = False

    #Generate c4
    active = True
    while active:
        n1 = random.randint(0,9)
        n2 = random.randint(0,9)
        n3 = random.randint(0,9)
        n4 = random.randint(0,9)
        if n1 - n2 - n3 - n4 > 0:
            chunk4 = str(n1)+str(n2)+str(n3)+str(n4)
            active = False
        

    #ASSEMBLE
    final_code = chunk1 + "-" + str(chunk2) + "-" + str(chunk3) + "-" + str(chunk4)
    print("Generated Code:")
    print(final_code)
