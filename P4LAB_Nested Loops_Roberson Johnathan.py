#CTI-110
#P4LAB_Nested Loops
#Roberson, Johnathan
#03/25/2018
#
#Import turtle
import turtle
#Add some style
turtle.shape("turtle")
turtle.color("green")
#Postion turtle so it can start going upward for its first movement
turtle.left(90)
#Create a for loop to repeat a setp 6 times
for i in range(6):
#Build the branch to be repeated 6 times
    turtle.forward(55)
    turtle.right(30)
    turtle.forward(45)
    turtle.back(45)
    turtle.left(30)
    turtle.forward(45)
    turtle.back(45)
    turtle.left(30)
    turtle.forward(45)
    turtle.back(45)
    turtle.right(30)
    turtle.back(55)
    turtle.left(60)
    
