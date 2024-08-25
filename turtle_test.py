import turtle

# Create a screen
screen = turtle.Screen()

# Create a turtle
my_turtle = turtle.Turtle()

# Draw a square
for _ in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)

# Close the window on click
screen.mainloop()
