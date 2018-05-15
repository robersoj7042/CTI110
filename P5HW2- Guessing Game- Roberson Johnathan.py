#CTI-110
#P5HW2- Test Average and Grades
#Roberson, Johnathan R
#04/22/2018
#
#Establish main function
def main():
    #Initiate play game function
    play_game()
    #Ask user if they would like to play again
    question = input('Play again? (y for yes, n for no): ')
    #Start while loop to always play game again if user answers "y"
    while question == 'y':
        play_game()
        #Ask question again after the play game function is started in the while loop
        question = input('Play again? (y for yes, n for no): ')
    #Use if statement in case user says "n" or anything else    
    if question == 'n':
        print('Thanks for playing my game!')
    else:
        print("I don't understand your response, please try again")
#Establish play game function
def play_game():
    #Generate random number
    import random
    for number in range(10):
        number = random.randint(1,101)
    choice = 0
    #Start while loop to end if user guesses number
    while choice != number:
        #Prompt user to guess number
        choice = float(input('Guess a number between 1 and 100: '))
        #Use if statement to give guidance to user and ask them to guess again
        if choice > number:
            print('Too high, try again')
        elif choice < number:
            print('Too low, try again')
        else:
            print('Congratulations! You guessed the correct number!')
#Initiate main function
main()
