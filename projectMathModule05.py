'''
##########################################################################
## Name........: Joseph Mischuck                                        ##
## Date Written: 2/5/2022                                               ##
## Purpose.....: Create a function that takes 3 numbers as input,       ##
##               and outputs the results of addition, division, and     ##
##               exponential powers.                                    ##
##########################################################################
'''


def main():



    # Takes the inputs #
    num1 = 13
    num2 = 5
    num3 = 3


    # Calculates and prints the sum #
    sum = num1 + num2 + num3
    print("\nThe sum of the three numbers is", sum)


    # Calculates and prints the remainder #
    remainder = num1 % num2
    print("\nThe remainder of the first number divided by the second number is", remainder)


    # Raises the second variable to the 3rd power #
    secondToTheThird = num2 ** 3
    print("\nThe second number raised to the third power is", secondToTheThird)


    # Does integer division on the first variable by the integer 4 #
    intDiv = num1 // 4
    print("\nThe first number divided by 4 is", intDiv)



main()