from enum import Enum

grid = []

class Dir(Enum):
    NORTH = -1, 0,
    EAST = 0, 1,
    SOUTH = 1, 0,
    WEST = 0, -1
    
def getGrid():
    
    with open('./2024/06/input.txt', 'r') as file:
        raw = file.read()
    
    rows = raw.split("\n")
    
    for i in range(len(rows)):
        gridRow = []
        
        for j in range(len(rows[i])):
            if rows[i][j] == '#':
                gridRow.append(1)
            elif rows[i][j] == '^':
                row, col = i, j
                gridRow.append(0)
            else:
                gridRow.append(0)
        
        grid.append(gridRow)
        
    return row, col

def getVisited(row, col, dir):
    
    visited = set()
    oob = False
    
    while not oob:
        visited.add((row, col))
        row, col, dir, oob = step(row, col, dir)
    
    return visited

def step(row, col, dir):
    rMov, cMov = dir.value
    
    row += rMov
    col += cMov
    
    if row < 0 or row > len(grid) - 1 or col < 0 or col > len(grid[row]) - 1:
        return None, None, None, True
    elif grid[row][col] == 1:
        
        row -= rMov
        col -= cMov
        
        if dir == Dir.NORTH:
            return step(row, col, Dir.EAST)
        elif dir == Dir.EAST:
            return step(row, col, Dir.SOUTH)
        elif dir == Dir.SOUTH:
            return step(row, col, Dir.WEST)
        elif dir == Dir.WEST:
            return step(row, col, Dir.NORTH)
    
    return row, col, dir, False

def checkElemLoop(row, col, pRow, pCol, dir):
    
    loop = False
    
    grid[pRow][pCol] = 1
    
    if checkLoop(row, col, dir):
        loop = True
    
    grid[pRow][pCol] = 0
    
    return loop

def checkLoop(row, col, dir):
    
    row1, col1, dir1 = row, col, dir
    row2, col2, dir2, oob = step(row, col, dir)
    
    if oob:
        return False
        
    while row1 != row2 or col1 != col2 or dir1 != dir2:
        row1, col1, dir1, _ = step(row1, col1, dir1)
        row2, col2, dir2, oob = step(row2, col2, dir2)
        
        if oob:
            return False
        
        row2, col2, dir2, oob = step(row2, col2, dir2)
        
        if oob:
            return False
    
    
    return True
        
def partOne():
    answer = 0
    
    row, col = getGrid()
    dir = Dir.NORTH
    
    answer = len(getVisited(row, col, dir))
    
    return answer

def partTwo():
    answer = 0
    
    row, col = getGrid()
    dir = Dir.NORTH
    
    visited = getVisited(row, col, dir)
    visited.remove((row, col))
    
    for pos in visited:
        pRow, pCol = pos
        
        if checkElemLoop(row, col, pRow, pCol, dir):
            answer += 1
    
    return answer

# HEAVELY inspired by liamasman solution at https://github.com/liamasman/advent-of-code-2024/blob/main/src/day_six.py
if __name__ == "__main__":
    print(f'The answer for part one is: {partOne()}')
    print(f'The answer for part two is: {partTwo()}')