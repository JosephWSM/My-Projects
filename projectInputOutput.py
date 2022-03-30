"""
##################################################################################################################
## Name........: Joseph Mischuck                                                                                ##
## Date Written: 2/5/2022                                                                                       ##
## Purpose.....: Creating a project that takes multiple inputs from a user and gives them different outputs     ##
##               calculated from their inputs.                                                                  ##
##################################################################################################################
"""



def main():



    # Initializes the variables for first name, last name, height, weight, and number of runs #
    firstName = ""
    lastName = ""
    userHeight = 0
    userWeight = 0
    numOfRuns = 0


    # Collects user input for first name and last name and converts the input to string #
    firstName = str(input("Hi there!, what is your first name? "))
    lastName = str(input("And what is your last name? "))

    # Outputs a message to the user stating their full name #
    print("\nNice to meet you", firstName + " " + lastName)


    # Collects user input for height, weight, and how many days they have ran #
    userHeight = float(input("\nHow tall are you in feet? "))
    userWeight = float(input("\nHow much do you weigh in lbs? "))
    numOfRuns = float(input("\nHow many days have you gone for a run? "))


    # Sets the values to the variables for stool height and number of stools, chair height and number of chairs, #
    # as well as the equation for the total height based on the user's input and previously mentioned variables. #
    stoolHeight = 1.5
    chairHeight = 3.4
    stoolNum = 3
    chairNum = 2
    stoolChairYouHeight = userHeight + (stoolNum * stoolHeight) + (chairNum * chairHeight)


    # Sets the value of pounds lost per run and calculates the user's weight after they input their weight #
    # and number of runs.                                                                                  #
    poundsLostPerRun = 0.5
    poundsLostPerRunCalculated = userWeight - (numOfRuns * poundsLostPerRun)


    # Outputs the user's weight and height including stools and chairs after the previous calculations #
    print("\nAfter all your runs, you will weigh", poundsLostPerRunCalculated, "lbs.")

    print("\nIf you were to stand on", stoolNum, "stools and", chairNum, "chairs you would be", stoolChairYouHeight, "feet tall.")



main()