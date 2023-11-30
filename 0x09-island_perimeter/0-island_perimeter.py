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
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            if grid[i][j] == 0:
                continue
            if grid[i][j + 1] == 0:
                perimeter += 1
                print(grid[i][j + 1], f"i = {i}: j + 1 = {j + 1}")
            if grid[i][j - 1] == 0:
                perimeter += 1
                print(grid[i][j - 1], f"i = {i}: j - 1 = {j - 1}")
            if grid[i + 1][j] == 0:
                perimeter += 1
                print(grid[i + 1][j], f"i + 1 = {i + 1}: j = {j}")
            if grid[i - 1][j] == 0:
                perimeter += 1
                print(grid[i - 1][j], f"i - 1 = {i - 1}: j = {j}")
    return perimeter
