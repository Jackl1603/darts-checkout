import numpy as np
from board import score        # reuse your own function from board.py

rng = np.random.default_rng()

def throw(aim_x, aim_y, sigma):
    pointx =  rng.normal(aim_x,sigma)
    pointy = rng.normal(aim_y, sigma)
    return pointx, pointy

def average_score(aim_x, aim_y, sigma, n):
    total = 0
    for i in range(n):
        x,y = throw(aim_x, aim_y, sigma)
        total += score(x,y)
    return total/n

print(average_score(0, 103, 60, 10000))   # aiming at treble 20
print(average_score(0, 0, 60, 10000))     # aiming at the bull))