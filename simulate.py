import numpy as np
import time
from board import score, score_many       # reuse your own function from board.py

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

def average_score_fast(aim_x, aim_y, sigma, n):
    xs  = rng.normal(aim_x, sigma, n)
    ys = rng.normal(aim_y, sigma, n)
    return score_many(xs, ys).mean()


if __name__ == "__main__":
    start = time.time()
    print(average_score(0, 103, 30, 10000))
    print("loop:", time.time() - start, "seconds")

    start = time.time()
    print(average_score_fast(0, 103, 30, 10000))
    print("fast:", time.time() - start, "seconds")

