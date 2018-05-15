#CTI-110
#P4HW3- Factorial
#Roberson, Johnathan R
#04/22/2018
#
#Prompt the user to enter a number
number = int(input('Enter a nonnegative integer? '))
factorial = 1
#Use For statement to keep multiplying until the count reaches the number entered
for x in range(1,number+1):
        #Multiply every number between 1 and the number
	factorial = factorial * x
#Display the value of the factorial	
print ('The factorial of', number, 'is ', factorial)

