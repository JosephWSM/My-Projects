'''
#############################################################################################
##  Written By..: Joseph Mischuck                                                          ##
##  Date Written: 3/9/2022                                                                 ##
##  Purpose.....: Demonstrate comprehension of for loops by obtaining user input           ##
##                and create a right triangle and upside down right triangle based on      ##
##                the inputs gathered from the user.                                       ##
#############################################################################################
'''



def main():

    # This is where I will initialize my variables

    userNum = 0
    userChar = 0
    i = 0
    j = 0

    # This is where I will set the range for the function

    min = 1
    max = 50
    step = 1


    # This is where I will obtain the user input for the number

    userNum = int(input("\nHi there, I'm gonna show you a magic trick today!\n\nGive me any number between 1 and 50: "))


    # This is where I will validate that the input is within the range
    # and then create my for loop for the triangles

    if userNum in range(min, max):
        userChar = input("\nThanks!, now give me any character on the keyboard: ")
        print("\naaaaaaaand.... ")
        print("\n...")
        print("...")
        print("...")
        print("\n...")
        print("")
        print("...")
        print("...")
        print("...")
        print("\nHold on, is this thing working?")
        print("...")
        print("...")
        print("\nThere we go,")
        print("...")
        print("...")
        print("\nVoila!\n")
        for i in range(userNum):
            for j in range(i + step):
                print(userChar, end='')
            print("")
    else:
        print("\nI said put a number between 1 and 50 dummy! Let's try this again.")
        while True:
            main()

    if userNum in range(min, max):
        print("")
        for i in range(userNum):
            print(userChar * (userNum - i))





main()