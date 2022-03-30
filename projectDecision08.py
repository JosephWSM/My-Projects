'''
#######################################################################################################################
##  Name........: Joe Mischuck                                                                                       ##
##  Date Written: 02/19/22                                                                                           ##
##  Purpose.....: Use decision statements to process an input, and output one of three colors, based on the input    ##
#######################################################################################################################
'''



def main():


    # Initialize variables here

    userInput = 0


    # Collect input from user here

    userInput = int(input("Enter a number here: "))


    # Decide if input is even here

    if (userInput % 2 == 0):
        print("\n\tYour number is even!")
    else:
        print("\n\tYour number is odd!")


    # Decide if input is a multiple of 3

    if (userInput % 3 == 0):
        print("\n\tYour number is a multiple of 3!")
    else:
        print("\n\tYour number is not a multiple of 3!")


    # Decide if number is below, in, or above the teens

    if (userInput <= 12 ):
        print("\n\tYour number is below the teens!")
    elif (userInput >= 20):
        print("\n\tYour number is above the teens!")
    else:
        print("\n\tYour number is in the teens!")


    # Decide if the number is represented by red, white, or blue

    if (userInput < 10):
        print("\n\tThe color based on ", userInput, "is red!")
    elif (userInput >= 20):
        print("\n\tThe color based on ", userInput, "is blue!")
    else:
        print("\n\tThe color based on ", userInput, "is white!")




main()