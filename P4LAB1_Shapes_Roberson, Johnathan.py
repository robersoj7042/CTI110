#CTI-110
#P4T1 - Turtle Lab
#Roberson, Johnathan
#03/23/2018
#
#Start by importing the turtle
import turtle
#Add a little character
turtle.shape("turtle")
turtle.color("purple")
#Get to a starting postion
turtle.penup()
turtle.forward(100)
turtle.pendown()
#Start first while loop for triangle
count = 0
while count < 3:
    turtle.forward(100)
    turtle.left(120)
    count = count +1
#One color is too boring
turtle.color("red")
#Get to next starting position
turtle.penup()
turtle.right(180)
turtle.forward(300)
turtle.pendown()
turtle.right(180)
#Start next while loop for square
count = 0
while count < 4:
    turtle.forward(100)
    turtle.left(90)
    count = count + 1
turtle.penup()
#Celebrate
turtle.forward(200)
count = 0
while count < 5:
    turtle.right(90)
    turtle.color("blue")
    turtle.right(90)
    turtle.color("purple")
    turtle.right(90)
    turtle.color("green")
    turtle.right(90)
    turtle.color("red")
    count = count + 1
turtle.left(90)
