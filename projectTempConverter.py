'''
####################################################################################
##  Written By..: Joseph Mischuck                                                 ##
##  Date Written: 3/23/22                                                         ##
##  Purpose.....: Create a temperature converter by demonstrating knowledge       ##
##                of functions and decision statements.                           ##
####################################################################################
'''




#--------------------------------------------------------------------------------------------------------------------
def main():
    # The main function, where all the magic happens

    value = 0 # This will hold the next or current temperature
    valueC = 0 # This will hold the current value in Celsius
    valueCHigh = 0  # This will hold the current high value in Celsius
    valueCLow = 0 # This will hold the current low value in Celsius
    valueCAvg = 0   # This will hold the current average value in Celsius
    low = 0 # This will hold the lowest value
    high = 0 # This will hold the highest value
    avg = 0 # Holds the average temp
    total = 0 # Keeps a total of all the temps inputted so far
    count = 0 # keeps track of how many inputs have been made



    while(value != -999):
        # This While loop keeps the program running until the user enters -999
        value = float(input("\nEnter the current temp (F) or -999 to quit: "))
        count += 1
        if(value != -999):
            if(count == 1):
                high = value
                low = value
            if(value > high):
                high = value
            if(value < low):
                low = value
            total += value
            avg = total / count
            valueC = getValueC(valueC, value)
            valueCHigh = getValueCHigh(high, valueCHigh)
            valueCLow = getValueCLow(low, valueCLow)
            valueCAvg = getValueCAvg(avg, valueCAvg)
            displayOutput(value, low, high, avg, valueC, valueCHigh, valueCLow, valueCAvg)
        else:
            print("\nHave a nice day.............")



#--------------------------------------------------------------------------------------------------------------------
# This function will display the output for all values in Fahrenheit and Celsius
def displayOutput(value, low, high, avg, valueC, valueCHigh, valueCLow, valueCAvg):

    getValueC(valueC, value)
    print("\n****** Temperature Output ******")
    print("Current Temperature: \t\t\t{0:.2f} F\t\t".format(value), end="")
    print("{0:.2f} C\t".format(valueC))

    getValueCHigh(high, valueCHigh)
    print("Highest Temperature so far: \t{0:.2f} F\t\t".format(high), end="")
    print("{0:.2f} C\t".format(valueCHigh))

    getValueCLow(low, valueCLow)
    print("Lowest Temperature so far: \t\t{0:.2f} F\t\t".format(low), end="")
    print("{0:.2f} C\t".format(valueCLow))

    getValueCAvg(avg, valueCAvg)
    print("Average Temperature so far: \t{0:.2f} F\t\t".format(avg), end="")
    print("{0:.2f} C\t".format(valueCAvg))



#--------------------------------------------------------------------------------------------------------------------
#This function will convert the value from Fahrenheit to Celsius
def getValueC(valueC, value):
    valueC = (value - 32) * 5/9
    return valueC



#--------------------------------------------------------------------------------------------------------------------
#This function will convert the average value from Fahrenheit to Celsius
def getValueCAvg(avg, valueCAvg):
    valueCAvg = (avg - 32) * 5/9
    return valueCAvg



#--------------------------------------------------------------------------------------------------------------------
#This function will convert the high value from Fahrenheit to Celsius
def getValueCHigh(high, valueCHigh):
    valueCHigh = (high - 32) * 5/9
    return valueCHigh



#--------------------------------------------------------------------------------------------------------------------
#This function will convert the low value from Fahrenheit to Celsius
def getValueCLow(low, valueCLow):
    valueCLow = (low - 32) * 5/9
    return valueCLow


#--------------------------------------------------------------------------------------------------------------------




main()


