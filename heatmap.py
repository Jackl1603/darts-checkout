import numpy as np
from simulate import average_score_fast 
from board import ring, number

positions = np.linspace(-170, 170, 69) #linspace gets two bounds -170, 170 and creates even amount of numbers between them (69 numbers)
grid = np.zeros((69,69)) #creates 69 by 69 2D array

for i in range(len(positions)):                   #Loops through the 2D array (grid)
    for j in range(len(positions)):
        grid[i,j] = average_score_fast(positions[j], positions[i], 30, 2000)

i, j = np.unravel_index(grid.argmax(), grid.shape) #.argmax finds the position of the highest value in the grid rathen that the value itself (.max)
                                                   #np.unravel_index(1,grid.shape) turns the 'long line' count back into (row, column), 
                                                   # uses grid.shape to see how wide each row is, 
                                                   # then the row and collumn of the best cell are put into i & j
best_x = positions[j]
best_y = positions[i]

r = ring(best_x,best_y)
n = number(best_x, best_y)

print("best aim:", best_x, best_y, r, n, grid.max())



print(grid[34, 34])    # the middle cell, aiming at the bull: about 13
print(grid.max())      # the best average score anywhere on the board
print(grid.shape)      # should be (69, 69)