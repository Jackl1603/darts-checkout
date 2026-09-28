# board.py - scoring a dart from where it lands on the board
import math
BULL_OUTER = 6.35
OUTER_BULL_OUTER = 15.9
TREBLE_INNER = 99
TREBLE_OUTER = 107
DOUBLE_INNER = 162
DOUBLE_OUTER = 170

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
    return a


print(angle(100, 0))    # right
print(angle(0, 100))    # up
print(angle(-100, 0))   # left
print(angle(0, -100))   # down



    
    



