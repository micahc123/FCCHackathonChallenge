import turtle
import random
import math

# Set up the screen
screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Kaleidoscope Pattern")
screen.tracer(0)  # Turn off animation for faster drawing

# Create the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
t.hideturtle()

# Color palette
colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#FDCB6E", "#6C5CE7", "#FF8ED4", "#FF3E4D", "#59C9A5"]

def draw_pattern(size, depth):
    if depth == 0:
        return
    
    angle = 360 / 6  # Hexagonal symmetry
    t.pencolor(random.choice(colors))
    
    for _ in range(6):
        t.forward(size)
        draw_pattern(size / 3, depth - 1)
        t.backward(size)
        t.right(angle)

def draw_kaleidoscope(num_patterns):
    for _ in range(num_patterns):
        t.penup()
        t.goto(0, 0)
        t.setheading(random.uniform(0, 360))
        t.pendown()
        draw_pattern(random.randint(50, 150), random.randint(2, 4))

    screen.update()

def animate_kaleidoscope():
    screen.clear()
    screen.bgcolor("black")
    draw_kaleidoscope(random.randint(5, 10))
    screen.ontimer(animate_kaleidoscope, 2000)  # Redraw every 2 seconds

# Start the animation
animate_kaleidoscope()

# Keep the window open
turtle.done()