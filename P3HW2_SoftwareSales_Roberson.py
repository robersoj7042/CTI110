#CTI-110
#P3HW2 - Software Sales
#Johnathan Roberson
#03/10/2018
#
#Get the amount of packages purchased
numofpacks = int(input('Enter the amount of packages purchased: '))
#Establish value of each package
packvalue = 99
#Calculate the discount
#Display the amount discounted
if numofpacks < 10:
    discountx = 1
    print('No discount was applied')
elif 10 <= numofpacks < 20:
    discountx = 0.9
    print('You recieved a 10% discount')
elif 20 <= numofpacks < 50:
    discountx = 0.8
    print('You recieved a 20% discount')
elif 50 <= numofpacks < 100:
    discountx = 0.7
    print('You recieved a 30% discount')
elif 100 <= numofpacks:
    discountx = 0.6
    print('You recieved a 40% discount')
#Find the toal cost after discount is applied
total = packvalue * numofpacks * discountx
#Display the total discount
print('Your total is: $', format(total,',.2f'))
