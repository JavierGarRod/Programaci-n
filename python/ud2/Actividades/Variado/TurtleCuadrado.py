import turtle

def pinta_cuadrado(color, lado,x,y):
    turtle.goto(x,y)

    for i in range(4):
        turtle.color(color)
        turtle.forward(lado)
        turtle.right(90)

pinta_cuadrado("blue", 100,0,0)
pinta_cuadrado("red", 100,200,200)
pinta_cuadrado("yellow",100,-200,-200)

turtle.hideturtle()
turtle.done()