#CTI-110
#P4T2- Bug Collector
#Roberson, Johnathan
#03/23/2018
#
# Initialize the accumulator.
total = 0

# Get the bugs collected for each day.
for day in range(1, 8):
    #prompt the user
    print('Enter the bugs collected on day', day)
    #input the numer of bugs
    bugs = int(input())
    #Add bugs to total
    total += bugs
# Display the total bugs.
print('You collected a total of', total, 'bugs')
