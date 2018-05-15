#CTI-110
#P4LAB2: Initials
#Roberson, Johnathan
#03/23/2018
#
#Import turtle
import turtle
#Get turtle into position
turtle.left(135)
turtle.penup()
turtle.forward(100)
turtle.right(135)
turtle.pendown()
#Start working on the letter "J"
turtle.forward(40)
turtle.back(20)
turtle.right(90)
turtle.forward(25)
#Establish while loop for the curve of the "J"
count = 0
while count < 3:
    turtle.right(45)
    turtle.forward(10)
    count = count + 1
#Get into postion for the "R"
turtle.penup()
#Establish while loop for back tracking the loop of the "J"
count = 0
while count < 3:
    turtle.back(10)
    turtle.left(45)
    count = count + 1
turtle.back(25)
turtle.left(90)
turtle.forward(35)
turtle.pendown()
#Establish while loop for the upper portion of the "R"
count = 0
while count < 4:
    turtle.forward(15)
    turtle.right(90)
    count = count + 1
#Draw the two legs of the "R"
turtle.right(90)
turtle.forward(32)
turtle.back(17)
turtle.left(45)
turtle.forward(25)
turtle.penup()
turtle.left(45)
turtle.forward(20)

