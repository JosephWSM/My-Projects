'''
###########################################################################################
##  Written By..: Joseph Mischuck                                                        ##
##  Date Written: 3/10/2022                                                              ##
##  Purpose.....: Create 3 functions to demonstrate capability to validate an integer,   ##
##                return a true or false value based on user input, and to identify      ##
##                the number of vowels present in a sentence input by the user.          ##
############################################################################################
'''


def main():



     userAge = 0
     min = 21
     max = 99



    # Creating a while loop to check input and make sure it is an integer, then return an output

     while True:
         try:
            userAge = int(input("\nHi there, how old are you? You must be between ages 21 and 99 to answer: "))
            break
         except:
             print("\nThats not an integer silly! Try again")
             main()
     if userAge in range(min, max):
         print("\nYou are", userAge, "years old.")
     else:
         print("\nI said between 21 and 99 you weirdo, not", userAge)
         main()




main()




def yesOrNo():



        #This is the function where we take y or n, whether lowercase or capital, and return true or false
    choice = "X"
    while (choice.capitalize() != "Y" and choice.capitalize() != "N"):

        choice = input("\nDo you think Dennis Hunchuck is an amazing professor?\n"
                       "\n[Y]es or [N]o\n"
                       "\nPlease place your answer here: ")

        if (choice.capitalize() == "N"):
            print("\n\tFalse :(")
        elif (choice.capitalize() == "Y"):
            print("\n\tTrue :)")
        else:
            print("\nPLEASE ANSWER WITH EITHER Y FOR yes OR N for no!!")

yesOrNo()




    # This is where we take a sentence and return the number of each type of vowel

def vowelCount():
    data = str(input("\nPlease type a sentence: "))
    vowels = "aeiou"
    print("\nThe vowels in this sentence are: ")

    for v in vowels:

        print(v, data.lower().count(v))







vowelCount()