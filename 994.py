from typing import List
import copy
'''

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

Example 1:
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
'''
class Solution:
    # O(x*y*t)
    ############################################################################
    def orangesRotting(self, grid: List[List[int]]) -> int:
        t=0
        while(True):
            new_rotten=False
            rotten_grid=copy.deepcopy(grid)
            for x in range(len(grid)):
                for y in range(len(grid[x])):
                    if grid[x][y]==1 and self.hasRottenNearBy(grid,x,y):
                        rotten_grid[x][y]=2
                        new_rotten=True
            if new_rotten:
                grid=copy.deepcopy(rotten_grid)
                rotten_grid.clear()
                t+=1
                continue
            else:
                if self.isAllRotten(rotten_grid):
                    return t
                else:
                    return -1
    def isAllRotten(self,grid):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    return False
        return True
    def hasRottenNearBy(self, grid, x,y):
        if x-1>=0  and grid[x-1][y]==2:
            return True
        elif y+1<len(grid[x]) and grid[x][y+1]==2:
            return True
        elif x+1<len(grid) and grid[x+1][y]==2:
            return True
        elif y-1>=0 and grid[x][y-1]==2:
            return True
        else:
            return False
    ###########################################################
class Solution2:
    # O(x*y)
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue=[]
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y]==2:
                    queue.append((x,y,0))
        t=0
        final_t=0
        while(queue):
            rotten= queue.pop(0)
            x,y,t=rotten
            if x-1>=0  and grid[x-1][y]==1:
                grid[x-1][y]=2
                queue.append((x-1,y,t+1))
                final_t=t+1
            if y+1<len(grid[x]) and grid[x][y+1]==1:
                grid[x][y+1]=2
                queue.append((x,y+1,t+1))
                final_t=t+1
            if x+1<len(grid) and grid[x+1][y]==1:
                grid[x+1][y]=2
                queue.append((x+1,y,t+1))
                final_t=t+1
            if y-1>=0 and grid[x][y-1]==1:
                print(x,y-1)
                grid[x][y-1]=2
                queue.append((x,y-1,t+1))
                final_t=t+1
        if self.isAllRotten(grid):
            return final_t
        else:
            return -1
    def isAllRotten(self,grid):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    return False
        return True
    
        
        