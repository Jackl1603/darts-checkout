import numpy as np
import matplotlib.pyplot as plt
from simulate import average_score_fast 
from board import ring, number, RING_EDGES, OUTER_BULL_OUTER, DOUBLE_OUTER

sigma = 30
positions = np.linspace(-170, 170, 69) #linspace gets two bounds -170, 170 and creates even amount of numbers between them (69 numbers)
grid = np.zeros((69,69)) #creates 69 by 69 2D array

for i in range(len(positions)):                   #Loops through the 2D array (grid)
    for j in range(len(positions)):
        grid[i,j] = average_score_fast(positions[j], positions[i], sigma, 2000)

i, j = np.unravel_index(grid.argmax(), grid.shape) #.argmax finds the position of the highest value in the grid rathen that the value itself (.max)
                                                   #np.unravel_index(1,grid.shape) turns the 'long line' count back into (row, column), 
                                                   # uses grid.shape to see how wide each row is, 
                                                   # then the row and collumn of the best cell are put into i & j
best_x = positions[j]      #turns the best cell's column and row numbers into an x position in mm
best_y = positions[i]

r = ring(best_x,best_y)          #finds which ring its in
n = number(best_x, best_y)       #finds the number value of the dart

print("best aim:", best_x, best_y, r, n, grid.max())


print(grid[34, 34])    
print(grid.max())      
print(grid.shape)    

plt.imshow(grid, origin="lower", extent=[-170,170,-170,170]) #colours each 69 x 69 cells by its average score: yellow for high and purple for low (heat)
                                 #origin="lower" -> puts row 0 at the bottom, withou this the board would come out upside down
                                 #extent tells the map the range the picture covers from left,right,bottom,top
         
plt.colorbar(label="Average points per dart")   #adds a key down the side showing which colour means which score
plt.title("Best place to aim: pub player (sigma 30mm)")
plt.xlabel("x position from centre (mm)")
plt.ylabel("y position from centre (mm)")
plt.plot(best_x, best_y, "rx", markersize=12)    #plots a redmark at the best spot for the player to aim for
plt.tight_layout()

   

for radius in RING_EDGES:
    circle = plt.Circle((0, 0), radius, fill=False, color ="white", linewidth = 0.8) #(0,0) centre, fill=false makes it an outline so we dont cover the heatmap
    plt.gca().add_patch(circle) # plt.gca()=get current axes, add_patch just puts the cirlce onto it



for i in range(20):     #loops for each 20 segments
    angle = 9 + 18 * i
    rad = np.radians(angle)   #converts the angle from degrees into radian because np (cos/sin) only understands radians
    x1 = OUTER_BULL_OUTER * np.cos(rad)  #finds the x point for the outerbull at every segement round the board ready to make the line
    y1 = OUTER_BULL_OUTER * np.sin(rad)  
    x2 = DOUBLE_OUTER * np.cos(rad)      #find the x point for the edge of the double at every segment to get the end of the line
    y2 = DOUBLE_OUTER * np.sin(rad)
    plt.plot([x1,x2],[y1, y2], color="white", linewidth=0.8)          #plots the line




    
plt.show()       #opens a window witht he picture