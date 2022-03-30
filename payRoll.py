'''
#####################################################################################
## Name: Joseph Mischuck                                                           ##
## Date: 02/15/2022                                                                ##
## Purpose: Making a program that will calculate the payroll for a small business. ##
#####################################################################################
'''


def main():



    # Get input here
    hourlyRate = float(input("Please enter the hourly rate provided by your employer: $"))
    hoursWorked = float(input("Please enter the amount of hours you worked: "))
    regPay = 0.0
    otPay = 0.0
    grossPay = 0.0
    fedTax = 0.0
    ssnoTax = 0.0
    netPay = 0.0
    annualPay = 0.0


    # Calculate regular and overtime pay here

    if(hoursWorked > 40):
        regPay = 40 * hourlyRate
        otPay = (hoursWorked - 40) * 1.5 * hourlyRate
    else:
        regPay = hoursWorked * hourlyRate
        otPay = 0.0


    # Calculate gross pay here

    grossPay = regPay + otPay


    # Calculate federal tax deduction here

    fedTax = grossPay * 0.12

    # Calculate social security tax deduction here

    ssnoTax = grossPay * 0.062

    # Calculate net pay here

    netPay = grossPay - fedTax - ssnoTax

    # Calculate annual pay

    annualPay = netPay * 52.1429


    # Display paycheck stub here

    print("Hourly Rate: ${0:,.2f}".format(hourlyRate))
    print("Hours Worked: {0:,.2f}".format(hoursWorked))
    print("Regular Pay: ${0:,.2f}".format(regPay))
    print("Overtime Pay: ${0:,.2f}".format(otPay))
    print("Gross Pay: ${0:,.2f}".format(grossPay))
    print("Federal Tax: ${0:,.2f}".format(fedTax))
    print("Social Security Tax: ${0:,.2f}".format(ssnoTax))
    print("Net Pay: ${0:,.2f}".format(netPay))
    print("Annual Pay: ${0:,.2f}".format(annualPay))




main()