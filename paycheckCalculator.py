'''
This asks the user for the pay period, asks how much the user makes per hour
this pay period, and then asks how many hours the user worked this week, in float
format. It then calculates overtime, and how much their paycheck will be.

Created By: Austin Garrett (MetaRollover)
'''


#list variables here
hourlyPay = 0
paycheck = 0
payPeriod = " "
payHistory = {}
loopIt = "y"
overtime = 0

#begin code here

#create loop to allow user to enter information mutliple times
while loopIt == 'y':
    #ask user period, pay, and hour information
    payPeriod = input("What pay period is this? (Example Date Format: 02/24/2018 - 03/02/2018)\n")
    hourlyPay = float(input("How much money did you make an hour during this period? \n(Please omit the $ sign.) \n"))
    hoursWorked = int(input("How many hours did you work during this week? \n(Enter in decimal values. Ex: If you worked 6hrs and 45mins, you would enter 6.75hrs)\n"))

    #check if hours is over 40

    #if 40 or under...
    if hoursWorked <= 40:
        paycheck = hoursWorked * hourlyPay
        payHistory[payPeriod] = paycheck

    #if over 40...
    else:
        overtime = float(input("How much were you paid for overtime? (Please omit the $ sign.)\n"))
        paycheck = (hourlyPay * 40) + ((hoursWorked - 40) * overtime)
        payHistory[payPeriod] = paycheck

    #print out pay history information
    for key, value in payHistory.items():
        print(key + "     " + str(value))

    #provide breakout for loop
    loopIt = input("Would you like to enter in another pay period? [y/n]")
