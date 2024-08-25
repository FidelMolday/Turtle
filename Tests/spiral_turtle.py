import turtle
import random

def draw_spiral(turtle_obj, size):
    for i in range(size):
        turtle_obj.forward(i * 3 / size + i)
        turtle_obj.left(59)
        turtle_obj.color(random.random(), random.random(), random.random())

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
spiral_turtle = turtle.Turtle()
spiral_turtle.speed(0)  # Fastest speed

# Draw a spiral
draw_spiral(spiral_turtle, 200) 

# Close the window on click
screen.mainloop()
