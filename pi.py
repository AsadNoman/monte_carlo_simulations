import random as rand
import math

m, n = 0, 0

while True:
    x, y = rand.random(), rand.random()
    if math.sqrt(x**2 + y**2) <= 1:
        n += 1
    m += 1
    print(f"{round(n*4/m, 6)}", end='\r')