#!/usr/bin/python3
"""
Defins the island_perimeter function
that returns the perimeter of an iland
(described as an array of integers)
"""


def island_perimeter(grid):
    """
        returns the perimeter of the island described in grid:

        @grid is a list of list of integers:
            *0 represents a water zone
            *1 represents a land zone
            *One cell is a square with side length 1
            *Grid cells are connected horizontally/vertically
             (not diagonally).
            *Grid is rectangular, width and height don’t exceed
             100
            *Grid is completely surrounded by water, and there is
             one island (or nothing).
            *The island doesn’t have “lakes” (water inside that
             isn’t connected to the water around the island).
    """

    y = 0
    x = 0

    # iterate through possible land mass
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[row]) - 1):
            if grid[row][col] == 1:
                # check if the box is near to the lake
                # either by left side, right side or both
                if grid[row][col - 1] == 0:
                    y += 1 # increment the length of vertical side
                if grid[row][col + 1] == 0:
                    y += 1

                # check if the box is near to the end/ lake
                # either by the top of the bottom
                if grid[row - 1][col] == 0:
                    x += 1 # increment the length of horizontal side
                if grid[row + 1][col] == 0:
                    x += 1
    return x + y # return the total length/ perimeter
