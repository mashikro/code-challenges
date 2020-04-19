# Prompt: Given a 2d grid map of '1's (land) and '0's (water), count the SUM  of 
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


def get_island_size(grid, i, j):
    if ((i < 0) or (i >= len(grid)) or (j < 0) or (j >= len(grid[i])) or (grid[i][j] == '0')):
        return 0
    sum_ = 0
    
    sum_+= int(grid[i][j])
    
    grid[i][j] = '0'

    sum_+=get_island_size(grid, i-1, j)
    sum_+=get_island_size(grid, i+1, j)
    sum_+=get_island_size(grid, i, j-1)
    sum_+=get_island_size(grid, i, j+1)

    return sum_


def find_num_islands(grid):
    if not grid:
        return 0 #empty list
    island_sums = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '1': #we actually wanna do something when we hit 1
                island_sums.append(get_island_size(grid, i, j))
    print(island_sums) 
    return island_sums



grid_1 = [['1','1','1','1','0'], ['1','1','0','1','0'], ['1','1','0','0','0'], ['0','0','0','0','0']]
grid_2 = [['1','1','0','0','0'], ['1','1','0','0','0'], ['0','0','1','0','0'], ['0','0','0','1','1']]
find_num_islands(grid_1) #[9]
find_num_islands(grid_2) #[4,1,2]
