import turtle as tu
import random as rand
import math

radius = 200
tu.hideturtle()

tu.tracer(0, 0)

tu.speed(0)

tu.screensize(500, 500)

tu.penup()
tu.goto(0, -radius)
tu.pendown()

tu.pencolor(0.8, 0.8, 0.8)
tu.circle(radius)
tu.pencolor(0.0, 0.0, 0.0)

tu.penup()
tu.goto(0,0)
tu.pendown()

for i in range(4): 
    tu.forward(radius) 
    tu.left(90)

n = 0
m = 0
tu.penup()

def erasableWrite(tortoise, name, font, align, reuse=None):
    eraser = tu.Turtle() if reuse is None else reuse
    eraser.hideturtle()
    eraser.up()
    eraser.setposition(tortoise.position())
    eraser.write(name, font=font, align=align)
    return eraser

tu.goto(100,-30)
pitext = erasableWrite(tu, "0.00", font=("Hack", 12, "normal"), align="center")

while(True):

    if  not m == 0:
        tu.goto(100,-30)
        pitext.clear()
        pitext = erasableWrite(tu, f'{round(n*4/m, 5)}', font=("Hack", 12, "normal"), align="center", reuse=pitext)
    
    x, y = rand.random(), rand.random()

    tu.goto(x*radius,y*radius)
    
    if (x**2 + y**2) <= 1:
        n += 1
        tu.dot(1, 'blue')
    else:
        tu.dot(1, 'red')

    m += 1


tu.update()

tu.mainloop()