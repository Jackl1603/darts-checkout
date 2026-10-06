import numpy as np
import matplotlib.pyplot as plt
from simulate import average_score_fast
from board import ring, number, NUMBERS, RING_EDGES, OUTER_BULL_OUTER, DOUBLE_OUTER

positions = np.linspace(-200, 200, 81) #linspace gets two bounds -200, 200 and creates even amount of numbers between them (81 numbers, 5mm apart)


def make_heatmap(sigma):
    grid = np.zeros((len(positions), len(positions))) #creates 81 by 81 2D array (matches positions automatically)

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

    print(f"sigma {sigma}: best aim:", best_x, best_y, r, n, grid.max()) #makes sigma into an fstring which fills {sigma} with the variables actual value

    plt.imshow(grid, origin="lower", extent=[-200,200,-200,200]) #colours each 81 x 81 cells by its average score: yellow for high and purple for low (heat)
                                                                 #origin="lower" -> puts row 0 at the bottom, withou this the board would come out upside down
                                                                 #extent tells the map the range the picture covers from left,right,bottom,top

    plt.colorbar(label="Average points per dart")                #adds a key down the side showing which colour means which score
    plt.title(f"Best place to aim (sigma {sigma}mm)")
    plt.xlabel("x position from centre (mm)")
    plt.ylabel("y position from centre (mm)")
    plt.plot(best_x, best_y, "rx", markersize=12)                #plots a redmark at the best spot for the player to aim for

    for radius in RING_EDGES:
        circle = plt.Circle((0, 0), radius, fill=False, color ="white", linewidth = 0.8) #(0,0) centre, fill=false makes it an outline so we dont cover the heatmap
        plt.gca().add_patch(circle)                    # plt.gca() = get current axes, add_patch just puts the cirlce onto it

    for i in range(20):     #loops for each 20 segments
        angle = 9 + 18 * i
        rad = np.radians(angle)   #converts the angle from degrees into radian because np (cos/sin) only understands radians
        x1 = OUTER_BULL_OUTER * np.cos(rad)  #finds the x point for the outerbull at every segement round the board ready to make the line
        y1 = OUTER_BULL_OUTER * np.sin(rad)
        x2 = DOUBLE_OUTER * np.cos(rad)      #find the x point for the edge of the double at every segment to get the end of the line
        y2 = DOUBLE_OUTER * np.sin(rad)
        plt.plot([x1,x2],[y1, y2], color="white", linewidth=0.8)          #plots the line

    for i in range(20):
        angle = 18 * i
        rad = np.radians(angle)
        x = 185 * np.cos(rad)
        y = 185 * np.sin(rad)
        plt.text(x, y, str(NUMBERS[i]), color="white", ha="center", va="center")

    plt.xlim(-200, 200)
    plt.ylim(-200, 200)   #increases boarder limit of heatmap
    plt.tight_layout() 
    plt.savefig(f"heatmap_sigma{sigma}.png", dpi=150)     #saves it as a png file, dpi is the sharpness
    plt.close()


for sigma in [5, 30, 60]: #creates a heatmap for each 3 levels of player from sigma 5 to 60
    make_heatmap(sigma)