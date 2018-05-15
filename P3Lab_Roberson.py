#CTI-110
#P3Lab
#Roberson, Johnathan
#03/10/2018
# I was supposed to put a comment here
# My Last Name

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    # TO DO: define the rest of the scores

    
    score = int(input('Enter grade: '))

    if score >= 90:
        print('Your grade is: A')
    elif 80 <= score < 90:
        print('Your grade is: B')
    elif 70 <= score < 80:
        print('Your grade is: C')

    elif score < 70:
        print('Your grade is: F')
# TO DO: finish this







# program start
main()
