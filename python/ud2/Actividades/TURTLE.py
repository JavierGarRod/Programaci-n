import turtle

def pinta_linea(color, largo, posx, posy):
    turtle.color(color) #definimos el color
    turtle.forward(largo) #definimos el largo
    turtle.speed(5) #definimos la velocidad

    turtle.pendown()
    turtle.goto(posx,posy)
    turtle.penup()

pinta_linea("blue", 50,0,0)
pinta_linea("red", 500,150,150)

for i in range(4):
    pinta_linea("blue", 50,0,0)
    turtle.right(90)
    
turtle.hideturtle()
turtle.done()