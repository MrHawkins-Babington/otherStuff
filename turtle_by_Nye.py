#Always import python modules like turtle first
import turtle

shape = int(input('''\nPlease enter a shape:
3 = triangle
4 = square
5 = pentagon\n'''))

if shape == 3 :
    for (n) in range(3):
        turtle.left(120)
        turtle.forward(100) 

elif shape == 4:
    for (n) in range(4):
        turtle.forward(100)
        turtle.right(90) 

elif shape == 5:
    for (n) in range(5):
        turtle.left(72)
        turtle.forward(100) 
