import turtle as tu
import random as rand
import math

tu.hideturtle()
tu.tracer(0, 0)
tu.speed(0)
tu.screensize(500, 500)

def irregular_shape():
    tu.pencolor('green')
    tu.penup()
    tu.goto(50, -50)

    tu.pendown()
    tu.right(90)
    tu.fd(50)
    tu.left(45)
    tu.fd(60)
    tu.left(90)
    tu.fd(40)
    tu.left(45)
    tu.fd(120)
    tu.right(45)
    tu.fd(30)
    for x in range(80):
        tu.forward(1)
        tu.left(1)
    tu.left(55)
    tu.fd(20)
    tu.right(45)
    tu.fd(20)
    tu.left(45)
    tu.fd(30)
    tu.right(45)
    tu.fd(20)
    tu.left(90)
    tu.fd(20)
    tu.right(45)
    for x in range(80):
        tu.forward(1)
        tu.left(1)
    tu.right(80)
    tu.fd(140)
    for x in range(80):
        tu.forward(1)
        tu.left(1)
    tu.left(10)
    tu.fd(10)
    tu.right(45)
    tu.fd(20)
    tu.left(90)
    tu.fd(20)
    tu.right(45)
    tu.fd(97)
    tu.left(45)
    tu.fd(40)
    tu.left(90)
    tu.fd(60)
    tu.left(45)
    tu.fd(50)
    tu.right(90)
    tu.fd(176)

def square():
    tu.pencolor(0.0, 0.0, 0.0)
    tu.penup()
    tu.goto(-220, -150)
    tu.pendown() 

    tu.forward(390) 
    tu.left(90)
    tu.forward(290) 
    tu.left(90)
    tu.forward(390) 
    tu.left(90)
    tu.forward(290) 
    tu.left(90)

def get_pixel_color(x, y):
    y = -y
    canvas = tu.getcanvas()
    ids = canvas.find_overlapping(x, y, x, y)

    if ids: 
        index = ids[-1]
        color = canvas.itemcget(index, "fill")
        if color:
            return color

    return "white"


irregular_shape()
square()

def erasableWrite(tortoise, name, font, align, reuse=None):
    eraser = tu.Turtle() if reuse is None else reuse
    eraser.hideturtle()
    eraser.up()
    eraser.setposition(tortoise.position())
    eraser.write(name, font=font, align=align)
    return eraser

tu.penup()
tu.goto(0,200)
pitext = erasableWrite(tu, "0.00", font=("Hack", 12, "normal"), align="center")
n, m = 0, 0
while True:
    tu.penup()
    x, y = rand.randint(-220, 170), rand.randint(-150, 140)
    
    xx = -220
    sides = 0
    consecutive = 0
    
    while xx < x:
        if get_pixel_color(xx, y) == 'green':
            if consecutive == 0:
                sides += 1
            consecutive = 1
            xx += 2
        else:
            consecutive = 0
        xx += 1

    if sides%2 == 1:
        tu.pencolor('red')
        n += 1
    else:
        tu.pencolor('blue')
    
    m += 1
    
    if not get_pixel_color(x, y) == 'green':
        tu.goto(x, y)
        tu.dot(1)
    
    tu.goto(-20, -180)
    pitext.clear()
    pitext = erasableWrite(tu, f'A = {int(n*113100/m)}', font=("Hack", 12, "normal"), align="center", reuse=pitext)

tu.update()
tu.mainloop()

    


