#start of script

#Variables
def gettarget():
    with open("/home/bluejay/Documents/Python Projects/Budget The Conqueror/targetdistance.txt") as tarfile:
        global tar_dist
        tar_dist = tarfile.read()
        tar_dist = float(tar_dist)
    
def getcomp():
    with open("/home/bluejay/Documents/Python Projects/Budget The Conqueror/compdist.txt") as compfile:
        global comp_dist
        comp_dist = compfile.read()
        comp_dist = float(comp_dist)


#Functions
def checkifcompleted():
    p_comp = comp_dist/tar_dist
    if p_comp >= 1:
        return True
    else:
        return False
    #checks if user has completed course

#main
while True:

    #get mode
    print("\n")
    print("Type 'add' to add distance or 'view' to view distance.")
    mode = input("Alternatively, type 'end' to exit program: ")

    #clean input
    mode = mode.lower()

    #get distance variables
    gettarget()
    getcomp()

    #main loop
    if checkifcompleted() == True:
        print("You have already completed this course.")
        break

    elif mode == "add":
        add_dist = float(input("Distance to add: "))
        write_dist = comp_dist + add_dist
        write_dist = str(write_dist)
        addcomp = open("/home/bluejay/Documents/Python Projects/Budget The Conqueror/compdist.txt", "w")
        addcomp.write(write_dist)
        print("Miles Logged!")
        addcomp.close()

    elif mode == "view":
        print("\n")
        print(comp_dist, "miles out of", tar_dist, "miles completed")
        print("---", '{:.2%}'.format(comp_dist/tar_dist), "Completed", "---")

    elif mode == "end":
        print("Loop Broken.")
        break

    else:
        print("INPUTERROR")
    