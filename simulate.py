import numpy as np
from board import score        # reuse your own function from board.py

rng = np.random.default_rng()

def throw(aim_x, aim_y, sigma):
    pointx =  rng.normal(aim_x,sigma)
    pointy = rng.normal(aim_y, sigma)
    return pointx, pointy

x, y = throw(0, 103, 10)    # aim at treble 20, sigma 10
print(x, y, score(x, y))