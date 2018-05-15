#CTI-110
#P3HW1 - Age Classifier
#Roberson, Johnathan
#03/10/2018
#
# Get the age.
agex = int(input('Enter the age of this person: '))

#Determine if this person is an infant, child, teenager, or adult
if agex <= 1:
    print('This person is an infant')
if 1 < agex < 13:
    print('This person is a child')
if 13 <= agex < 20:
    print('This person is a teenager')
if agex >= 20:
    print('This person is an adult')
