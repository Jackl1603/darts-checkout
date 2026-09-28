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
          
print(ring(0, 0)) #bull
print(ring(0, 10))     # outer_bull
print(ring(0, 50))     # single
print(ring(60, 80))    # treble
print(ring(120, 0))    # single
print(ring(0, 165))    # double
print(ring(0, 200))    # miss




    
    



