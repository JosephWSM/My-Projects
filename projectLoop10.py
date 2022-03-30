'''
##################################################################################################################
##Written By: Joseph Mischuck                                                                                   ##
##Written on: 3/4/2022                                                                                          ##
##Purpose: Understand loop and decision statements, demonstrate logical program flow, and use/get random numbers##
##################################################################################################################
'''

import random

def main():

    #Here we are going to be defining and getting our variables

    i = 2
    ranNum = random.randint(1, 100)
    count = 0
    userName = input("\nHey there, if you would like to play a game just share with me your name: ")


    #Here we are going to introduce the user to the game and aquiring their number

    print("\nWelcome to my guessing game,", userName, "the rules are simple, there is a random number between 1 and 100"
          " and you have 10 tries to guess that number.\nI will let you know if you must go higher or lower"
          " but that's all you are getting out of me. GOOD LUCK!!")
    userNum = int(input("\nChoose a random number between 1 and 100: "))


    #This is where we will begin the loop, establish our conditions, count the amount of times we loop,
    #and guide our user through the game

    while (i <= 10):
        count = count + 1
        if (userNum >= 101 or userNum < 1):
            print('\033[91m' +"\nI said between 1 and 100 dude, you're losing a try for that"'\033[0m')
        if(ranNum == userNum):
            print("\nCongrats", userName, "you were able to guess that the number was",
                  ranNum, "in", count, "attempts, that's pretty impressive")
            break
        elif(userNum > ranNum):
            userNum = int(input("\nNot quite, take another guess but try guessing lower: "))
        elif(userNum < ranNum):
            userNum = int(input("\nNot quite, take another guess but try guessing higher: "))


    #Here we have our way of exiting the loop if the user is unable to guess the number

        i = i + 1


    #Lastly this is our condition that ends the loop after the 10th attempt and explains why to the user
        if(i == 11):
            print("\nSorry", userName, "unfortunately you ran out of guesses, the correct number was actually", ranNum)








main()