# board.py - scoring a dart from where it lands on the board
import math
import numpy as np       

BULL_OUTER = 6.35
OUTER_BULL_OUTER = 15.9
TREBLE_INNER = 99
TREBLE_OUTER = 107
DOUBLE_INNER = 162
DOUBLE_OUTER = 170

RING_EDGES = [BULL_OUTER, OUTER_BULL_OUTER, TREBLE_INNER, TREBLE_OUTER, DOUBLE_INNER, DOUBLE_OUTER]

NUMBERS = [6,13,4,18,1,20,5,12,9,14,11,8,16,7,19,3,17,2,15,10]

def ring(x, y):
    r = math.sqrt(x**2 + y**2)
    if r <= BULL_OUTER:
        return 'bull'
    elif r <= OUTER_BULL_OUTER:
        return 'outer_bull'
    elif r <= TREBLE_INNER:
        return 'single'        
    elif r <= TREBLE_OUTER:

        return 'treble'
    elif r <= DOUBLE_INNER:
        return 'single'        # outer single area
    elif r <= DOUBLE_OUTER:
        return 'double'
    else:
        return 'miss'

def angle(x,y):
    a = math.degrees(math.atan2(y,x)) # finds the angle from the centre
    return (a%360)

def number(x,y):
    a = angle(x,y)
    shifted = (a + 9) % 360
    segment = int(shifted // 18)
    return NUMBERS[segment]

def number_many(xs,ys):
    a = np.degrees(np.arctan2(ys, xs))
    shifted = (a + 9) % 360
    segment = (shifted // 18).astype(int)
    return np.array(NUMBERS)[segment]

def score(x,y):
    r = ring(x,y)
    n = number(x,y)
    if r == 'bull':
        return 50
    elif r == 'outer_bull':
        return 25
    elif r == 'treble':
        return n * 3
    elif r == 'double':
        return n*2
    elif r == 'miss':
        return 0
    else:
        return n


def score_many(xs,ys):
    r = np.sqrt(xs ** 2 + ys ** 2)
    n = number_many(xs, ys)
    return np.select([r <= BULL_OUTER, r <= OUTER_BULL_OUTER, r <= TREBLE_INNER, r <= TREBLE_OUTER, r<= DOUBLE_INNER, r<= DOUBLE_OUTER, r > DOUBLE_OUTER],
                     [50, 25, n, n*3, n, n*2, 0])


 

if __name__ == "__main__":
    print(score(0, 0))       # bull: 50
    print(score(0, 10))      # outer bull: 25
    print(score(0, 50))      # single 20: 20
    print(score(0, 103))     # treble 20: 60
    print(score(0, 165))     # double 20: 40
    print(score(-103, 0))    # treble 11: 33
    print(score(0, 200))     # miss: 0

    xs = np.array([0, 0, 0, 0, 0, -103, 0])
    ys = np.array([0, 10, 50, 103, 165, 0, 200])
    print(score_many(xs, ys))    # expect: [50 25 20 60 40 33  0]








    
    



