import turtle

# creating canvas 
turtle.Screen().bgcolor("Orange")

sc = turtle.Screen()
sc.setup(400, 300)

turtle.title("Welcome to Turtle window")

# turtle object creation
board = turtle.Turtle()

# creating a square
for i in range(4):
        board.forward(100)
        board.left(90)
        i = i+1
turtle.done()