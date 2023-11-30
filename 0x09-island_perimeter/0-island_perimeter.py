#!/usr/bin/python3
""" Island perimeter algorithm solution
"""

def island_perimeter(grid):
    """Calculate island perimeter based on the number of
    ones on the list of lists passed to the function

    Args:
        grid (List[List[int]]): grid that represents land

    Returns:
        int: whole perimeter of land
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if i <= 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                if i >= len(grid) - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                if j <= 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                if j >= len(grid[i]) - 1 or grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
