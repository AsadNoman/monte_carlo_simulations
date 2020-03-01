import turtle as tu
import random as rand
import math

fd, lt, rt = 0.5, 0.3, 0.2

angle = 90

tu.hideturtle()
tu.speed(0)
tu.screensize(500, 500)
tu.penup()

def erasableWrite(tortoise, name, font, align, reuse=None):
    eraser = tu.Turtle() if reuse is None else reuse
    eraser.hideturtle()
    eraser.up()
    eraser.setposition(tortoise.position())
    eraser.write(name, font=font, align=align)
    return eraser


tu.goto(-250, -250)
tu.pencolor(0.9, 0.9, 0.9)
tu.pendown()
for i in range(4): 
    tu.forward(500) 
    tu.left(90)


tu.penup()
shifts = 250
while shifts > 0:
    x, y = rand.randint(-250, 250), rand.randint(-250, 250)
    tu.goto(x,y)
    tu.pencolor('blue')
    tu.dot(3)
    shifts -= 1

tu.pencolor('black')
tu.pendown()

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


tu.penup()
tu.goto(0, -250)
tu.lt(90)


while True:
    r = rand.random()

    if r > fd:
        tu.fd(1)
    elif r > lt:
        tu.lt(90)
        tu.fd(1)
        tu.rt(90)
    else:
        tu.rt(90)
        tu.fd(1)
        tu.lt(90)
    
    if get_pixel_color(tu.pos()[0], tu.pos()[1]) == 'blue':
        angle = rand.randint(0, 180)
        direction = rand.choice(['left', 'right'])

        if direction == 'left':
            tu.left(angle)
        else:
            tu.right(angle)

    tu.dot(1)



tu.update()
tu.mainloop()
