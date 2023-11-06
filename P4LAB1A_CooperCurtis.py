#Curtis Cooper
#P4LAB1A
#November 5, 2023

import turtle

sam = turtle.Turtle()

sam.shape("turtle")

for num in range(4):
	sam.forward(50)
	sam.left(90)

sam.penup ()
sam.forward(100)
sam.pendown()

for num in range (3):
    sam.forward(50)
    sam.left(120)
