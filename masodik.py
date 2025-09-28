import turtle

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.color("white")

for i in range(5):
    t.forward(200)
    t.right(144)

def kilep():
    screen.bye()

screen.listen()
screen.onkey(kilep, "q")

turtle.done()