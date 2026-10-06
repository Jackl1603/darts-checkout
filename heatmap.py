import numpy as np
from simulate import average_score_fast 
positions = np.linspace(-170, 170, 69)
grid = np.zeros((69,69))

for i in range(len(positions)):
    for j in range(len(positions)):
        grid[i,j] = average_score_fast(positions[j], positions[i], 30, 2000)

print(grid[34, 34])    # the middle cell, aiming at the bull: about 13
print(grid.max())      # the best average score anywhere on the board
print(grid.shape)      # should be (69, 69)