import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create the turtle object
ronaldo = turtle.Turtle()
ronaldo.shape("turtle")
ronaldo.color("black")

# Draw Ronaldo's face
ronaldo.penup()
ronaldo.goto(0, -100)
ronaldo.pendown()
ronaldo.circle(100)

# Draw Ronaldo's eyes
ronaldo.penup()
ronaldo.goto(-40, 20)
ronaldo.pendown()
ronaldo.circle(20)
ronaldo.penup()
ronaldo.goto(40, 20)
ronaldo.pendown()
ronaldo.circle(20)

# Draw Ronaldo's mouth
ronaldo.penup()
ronaldo.goto(-40, -30)
ronaldo.pendown()
ronaldo.setheading(-60)
ronaldo.circle(40, 120)

# Draw Ronaldo's hair
ronaldo.penup()
ronaldo.goto(-70, 50)
ronaldo.pendown()
ronaldo.setheading(180)
ronaldo.forward(140)
ronaldo.setheading(120)
ronaldo.circle(-70, 240)
ronaldo.setheading(0)
ronaldo.forward(140)

# Hide the turtle
ronaldo.hideturtle()

# Exit on click
turtle.exitonclick()
