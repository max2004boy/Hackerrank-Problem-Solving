# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 12:15:34 2020

@author: max20
"""

def cavityMap(grid):
    grid_new = grid.copy()
    
    for i in range(1, len(grid)-1):
        row_temp = grid_new[i]
        for j in range(1, len(grid)-1):
            if int(grid[i][j]) > max(int(grid[i][j-1]), int(grid[i+1][j]), int(grid[i][j+1]), int(grid[i-1][j])):
                # replace with 'X' if a cavity point is found
                row_temp = row_temp[:j] + 'X' + row_temp[j+1:]
        grid_new[i] = row_temp
    
    return grid_new


if __name__ == '__main__':
    
    n = int(input())
    grid = []
    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    print('\n'.join(cavityMap(grid)))
