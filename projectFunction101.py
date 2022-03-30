'''
###########################################################################################
##  Written By..: Joseph Mischuck                                                        ##
##  Date Written: 3/24/22                                                                ##
##  Purpose.....: Create a program to return a value, not return a value, pass values    ##
##                and return multiple values using functions.                            ##
###########################################################################################
'''


#--------------------------------------------------------------------------------------------------------------------
def main():
# This is the main function. 'Nuff said.
    name = ""
    nameCount = 0

    name = getName(name)
    nameCount = displayNameTimesCount(name)
    evenOrOdd(nameCount)
    displayCountVariations(nameCount)

#--------------------------------------------------------------------------------------------------------------------
# This is the function that will display the number of letters in the name, that number squared, that number cubed, and the square root of that number.
def displayCountVariations(nameCount):
    print("\n\nThe number of letters in your name is:", nameCount)
    print("The number of letters in your name squared is:", nameCount ** 2)
    print("The number of letters in your name cubed is:", nameCount ** 3)
    print("The square root of the number of letters in your name is:", "{0:.3f}".format(nameCount ** 0.5))
#--------------------------------------------------------------------------------------------------------------------
# This is the function that will display the name the amount of times of the number of letters in the name.
def displayNameTimesCount(name):
    nameCount = len(name)
    print("\n")
    print (name * nameCount)
    return nameCount
#--------------------------------------------------------------------------------------------------------------------
# This is the function that will display whether the number of letters in the name is even or odd.
def evenOrOdd(nameCount):
    if (nameCount % 2 == 0):
        print("\n")
        print(nameCount, "is EVEN")
    else:
        print("\n")
        print(nameCount, "is ODD")
#--------------------------------------------------------------------------------------------------------------------
# This is the function that will get the input from the user to get their name.
def getName(name):
    name = str(input("Hi there, what is your name?: "))
    print("\nYour name is", name)
    return name

#--------------------------------------------------------------------------------------------------------------------





main()