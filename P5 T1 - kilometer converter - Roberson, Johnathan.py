#CTI-110
#P5T1 - kilometer converter
#Roberson, Johnathan r
#04-21-208
#

CONVERSION_FACTOR = 0.6214

def main():
    # Get the distance in kilometers.
    kilometers = float(input('Enter a distance in kilometers: '))

    # Display the distance converted to miles.
    show_miles(kilometers)

def show_miles(km):
    # Calculate miles.
    miles = km * CONVERSION_FACTOR

    # Display the miles.
    print(km, 'kilometers equals', miles, 'mile.')

main() 
