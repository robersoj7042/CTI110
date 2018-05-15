#CTI-110
#P4HW2- Running Total
#Roberson, Johnathan R
#04/22/2018
#
#Set values of variable to 0
total = 0
number = 0
#Start while loop to stop after a negative number is entered
while number >= 0:
    #Prompt user to acquire a number to add to total
    number = float(input('Enter a number? '))
    #Add all numbers entered
    total = total + number
    if number < 0:
        #Make sure the negative number is not added to total
        total = total - number
#Display total
print('Total:', total)
