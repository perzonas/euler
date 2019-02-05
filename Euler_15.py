# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?

def find_routes(grid_side):
    grid = [1] * grid_side
    for i in range(grid_side):
        for j in range(i):
            grid[j] = grid[j]+grid[j-1]
        grid[i] = 2 * grid[i - 1]
    return grid[grid_side - 1]


print(find_routes(20))
