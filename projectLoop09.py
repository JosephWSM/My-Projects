'''
#############################################################################
## Name...: Joseph Mischuck                                                ##
## Date...: 03/04/2022                                                     ##
## Purpose: Create a program that loops 101 times starting at 0,           ##
##          only displaying the odd increments.                            ##
#############################################################################
'''


def main():

    # Here is where I initialize the variable, "i" which will serve as my counter
    i = 0

    # This is where I create my while loop, as well as an if statement to determine whether
    # I have an output or not based on if the number is even or odd
    while(i <= 101):

        if (i % 2 != 0 ):
            print("{:>3}".format(i), ". Joseph.", sep='')

        i = i + 1





main()