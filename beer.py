'''
###############################################
## Author......: Joseph Mischuck             ##
## Date Written: 2/1/2022                    ##
## Purpose.....:                             ##
###############################################
'''

def main():
    CALORIESPERCAN = 125
    howMany = 0
    beerCost = 0.00

    # Get Input Here #
    howMany = int(input("How many beers do you drink a week?: "))
    beerCost = float(input("How much do you pay for a can of beer?: "))

    # Calculate Stuff Here #
    cansPerYear = howMany * 52
    costPerYear = cansPerYear * beerCost
    caloriesPerYear = cansPerYear * CALORIESPERCAN

    # Display Output Here #
    displayOutput(cansPerYear, costPerYear, caloriesPerYear)






def displayOutput(cansPerYear, costPerYear, caloriesPerYear):

    #print("You drank", cansPerYear,"beers last year.")
    print("\n\nYou drank {0:,} cans of beer last year.".format(cansPerYear))
    print("You consumed {0:,} calories last year.".format(caloriesPerYear))
    print("You spent $ {0:,.2f} last year.".format(costPerYear))














main()