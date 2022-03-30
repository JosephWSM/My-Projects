"""
#################################################################################
##Written By: Joseph Mischuck                                                  ##
##Written on: 2/25/2022                                                        ##
##Purpose: Create a program that displays a menu, takes the users inputs, and  ##
##         sends them to other inputs based on their menu selection, providing ##
##         them with even more outputs                                         ##
#################################################################################
"""

from datetime import date


def main():

    # This is where we will set up our menu and take data from the user,
    # this step also consists of our while loop where the only way out should be to [Quit]
    choice = "X"
    while choice.capitalize() != "Q":
        print("*** M A I N  M E N U ***")
        print("\n[N]ame")
        print("[A]ge")
        print("[D]ate")
        print("[Q]uit")
        choice = input("\nEnter your selection from menu: ")

    # This is where we will set up our [N]ame function, this should take the user's name and wish them a good day
        if choice.capitalize() == "N":
            name = input("\nWhat is your name? ")
            print("Hello", name + ", " "have a nice day.")

    # This is where we will have our [A]ge function, this function should be able to accept input from the user and
    # depending on the age given should spit out a phrase tailored to that age or nothing at all
        if choice.capitalize() == "A":
            age = int(input("\nHow old are you? "))
            yearsUntilLegal = 21 - age
            if age < 10:
                print("You are only", age, "I think it's past your bedtime.")
            elif 21 <= age < 60:
                print("Since you are", age, "let's go for a drink.")
            elif age >= 21 and age > 60:
                print("Since you are", age, "let's go for a drink.""\nWOW,", age, "is getting up there, gramps.")
            else:
                print(age, "is just a little too young, gotta wait", yearsUntilLegal, " more years until we can share a drink.")

    # This is where we will set up the [D]ate function where all we relay is the date to the user in the format of M/D/Y/
        if choice.capitalize() == "D":
            today = date.today()
            currentDate = today.strftime("%m/%d/%y")
            print("\nToday's date is:", currentDate)

    # This is where we will set up the [Q]uit function that allows the user to leave the loop and thanks them
        if choice.capitalize() == "Q":
            print("\nThanks for using my program and have a great day, unless you found a way to break it, then have a horrible day.")





main()