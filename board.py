# board.py - scoring a dart from where it lands on the board
import math
BULL_OUTER = 6.35
OUTER_BULL_OUTER = 15.9
TREBLE_INNER = 99
TREBLE_OUTER = 107
DOUBLE_INNER = 162
DOUBLE_OUTER = 170

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

print(number(0, 100))    # up: 20
print(number(100, 0))    # right: 6
print(number(-100, 0))   # left: 11
print(number(0, -100))   # down: 3
print(number(59, -81))   # bottom-right: 2
print(number(95, -31))   # just below the 6: 10



    
    



