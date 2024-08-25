import turtle

def draw_mandala(turtle_obj, num_petals, radius):
    angle = 360 / num_petals
    for _ in range(num_petals):
        turtle_obj.circle(radius)
        turtle_obj.left(angle)
        turtle_obj.color(random.random(), random.random(), random.random())

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
mandala_turtle = turtle.Turtle()
mandala_turtle.speed(0)  # Fastest speed

# Draw the mandala
draw_mandala(mandala_turtle, 36, 100)

# Close the window on click
screen.mainloop()
