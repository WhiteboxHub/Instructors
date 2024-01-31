import turtle
def setup():
    turtle.title('Multiple Squares Animation') 
    turtle.setup(100, 100, 0, 0)
    turtle.hideturtle()
def draw_square(size):
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
setup()
for _ in range(0, 12):
    draw_square(50)
    turtle.right(120)
    turtle.exitonclick()
