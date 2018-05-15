#CTI-110
#P4HW1- Distance Traveled
#Roberson, Johnathan
#03/25/2018
#Display all the distances a vehicle has traveled per hour given speed and time
#Promt the user to input the values for the speed and the time the vehicle traveled
print('What is the speed of the vehicle in mph?')
speed = int(input())
print('How many hours has it traveled?')
time = int(input())
#Display a table to organize output
print("Time     Distance Traveled")
print("--------------------------")
#Create while loop to list the distance given the speed
for time in range(1, time + 1):   
    distance = time * speed
    #Display the distance traveled for every hour that has passed
    print(time,"      ",distance)





