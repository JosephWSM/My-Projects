'''
#########################################################################################################
##  Written By..: Joseph Mischuck                                                                      ##
##  Date Written: 3/18/22                                                                              ##
##  Purpose.....: Create a program with a menu by writing, calling, and reusing functions.             ##
##                                                                                                     ##
#########################################################################################################
'''



def main():

    # This is where I initialize my variables
    number = 0
    low = 0
    high = 0
    sum = 0
    average = 0
    count = 0






    # This is the main while loop that will react to the user's input

    quit = False
    while (not quit):
        #This is the while loop that verifies that the user either presses G or Q, nothing else
        while (count == 0):
            userChoice = getSelection()
            if (userChoice == "G".lower()):
                number = getANumber(number)
                count += 1
                sum += number
                average = sum / count
            elif (userChoice == "Q".lower()):
                print("\nThanks for using my menu!")
                quit = True
                break
            else:
                print("\n" * 30,
                      "\n\n\nPlease pick G before any other selections like I advised, Thank you!" "\n*****************************************************************************")
                count == 0
            if (count == 1):
                high = number
                low = number
            if (number > high):
                high = number
            if (number < low):
                low = number
        while (count >= 1):
            userChoice = getSelection()
            if(userChoice == "G".lower()):
                number = getANumber(number)
                count += 1
                sum += number
                average = sum / count
            elif(userChoice == "S".lower()):
                showSum(sum)
            elif(userChoice == "A".lower()):
                showAverage(average)
            elif(userChoice == "H".lower()):
                showHighest(high)
            elif(userChoice == "L".lower()):
                showLowest(low)
            elif(userChoice == "Q".lower()):
                print("\nThanks for using my menu!")
                quit = True
                break
            else:
                print("\nInvalid selection. Please choose from the menu.")
            if (count == 1):
                high = number
                low = number
            if (number > high):
                high = number
            if (number < low):
                low = number





# This function gets the user's selection from the menu
def getSelection():
    displayMenu()
    result = input("\n\t Select a letter from the choices above: ").lower()
    return result

# This function gets the number when the user presses G
def getANumber(number):
    number = int(input("\nHi there! Give me any number you would like!: "))
    return number




# This is the function that will show the sum
def showSum(sum):
    print("\nThe sum of your numbers so far is:", sum)


# This is the function that will show the average
def showAverage(average):
    print("\nThe average of your numbers so far is:", average)


# This is the function that will show the highest number
def showHighest(high):
    print("\nThe highest number so far is:", high)


# This is the function that will show the lowest number
def showLowest(low):
    print("\nThe lowest number so far is:", low)


# This is the function that will display the menu
def displayMenu():
    print("\nWelcome to Joe's Number Menu! Make sure you input at least\none number from option G before choosing any of the other options!")

    print("\nG]  Get a number")
    print("\nS]  Show current sum of numbers")
    print("\nA]  Show current average of numbers")
    print("\nH]  Show the highest number")
    print("\nL]  Show the lowest number")
    print("\nQ]  Quit")






#########################################################################################################################
main()