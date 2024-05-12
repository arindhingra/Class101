import random 
userchoice = "yes"
while userchoice == "yes" or userchoice == "yeah" or userchoice == "ye": 
    num = random.randint(1,6)
    if num == 1: 
        print("your choice is 1")
    if num == 2: 
        print("your choice is 2")
    if num == 3: 
        print("your choice is 3")
    if num == 4: 
        print("your choice is 4")
    if num == 5: 
        print("your choice is 5")
    if num == 6: 
        print("your choice is 6")
    userchoice = input("yes to continue")
    print()