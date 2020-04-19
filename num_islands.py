# Prompt: Given a 2d grid map of '1's (land) and '0's (water), count the number of 
# islands. An island is surrounded by water and is formed by connecting 
# adjacent lands horizontally or vertically. You may assume all four edges 
# of the grid are all surrounded by water.

# Test Cases:

# Input1:
# 11110
# 11010
# 11000
# 00000

# Output1: 1

# Input2:
# 11000
# 11000
# 00100
# 00011

# Output2: 3


def clear_island(grid, i, j):
    if ((i < 0) or (i >= len(grid)) or (j < 0) or (j >= len(grid[i])) or (grid[i][j] == '0')):
        return 

    grid[i][j] = '0'

    clear_island(grid, i-1, j)
    clear_island(grid, i+1, j)
    clear_island(grid, i, j-1)
    clear_island(grid, i, j+1)



def find_num_islands(grid):
    if not grid:
        return 0 #empty list
    num_islands = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '1': #we actually wanna do something when we hit 1
                #Meat of algo: before we increment num_islands we need to check neigbors and make sure to not include them every count
                clear_island(grid, i, j)
                num_islands += 1 #helper func to check neighbors            
    print(num_islands) 
    return num_islands



grid_1 = [['1','1','1','1','0'], ['1','1','0','1','0'], ['1','1','0','0','0'], ['0','0','0','0','0']]
grid_2 = [['1','1','0','0','0'], ['1','1','0','0','0'], ['0','0','1','0','0'], ['0','0','0','1','1']]
find_num_islands(grid_1) #1
find_num_islands(grid_2) #3




