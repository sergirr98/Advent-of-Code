import heapq
from enum import Enum, auto

class Cell(Enum):
    Empty = auto()
    Wall = auto()

class Dir(Enum):
    UP = -1, 0
    RIGHT = 0, 1
    DOWN = 1, 0
    LEFT = 0, -1

map = []

def generateInput():
    
    with open('./2024/20/input.txt', 'r') as file:
        for i, line in enumerate(file):
            mapLine = []
            for j, elem in enumerate(line):
                if elem == '#':
                    mapLine.append(Cell.Wall)
                else:
                    mapLine.append(Cell.Empty)
                    
                    if elem == 'S':
                        start = (i, j)
                    elif elem == 'E':
                        end = (i, j)
                        
            map.append(mapLine)
                        
    return start, end

def printMap():
    for line in map:
        for elem in line:
            if elem == Cell.Empty:
                print('.', end='')
            elif elem == Cell.Wall:
                print('#', end='')
        
        print()

def Dijkstra(startingRow, startingCol):
    
    dist = dict()
    pq = []
    
    dist[(startingRow, startingCol)] = 0
    heapq.heappush(pq, (0, startingRow, startingCol))
    
    while pq:
        (d, row, col) = heapq.heappop(pq)
        
        if dist[(row, col)] < d:
            continue
        
        for dir in Dir:
            dRow, dCol = dir.value
        
            nextRow = row + dRow
            nextCol = col + dCol
            
            if (0 <= nextRow < len(map) and 0 <= nextCol < len(map[0])) and map[nextRow][nextCol] != Cell.Wall and ((nextRow, nextCol) not in dist or dist[(nextRow, nextCol)] > d + 1):
                nextS = d + 1
                dist[(nextRow, nextCol)] = nextS
                heapq.heappush(pq, (nextS, nextRow, nextCol))
        
    return dist

def manhattan(start, end):
    startRow, startCol = start
    endRow, endCol = end
    
    return int(abs(startRow - endRow) + abs(startCol - endCol))

def getOptimalPath(distFromStart, distFromEnd, optimal):
    result = set()
    
    for row in range(len(map)):
        for col in range(len(map[row])):
            stateFromStart = (row, col)
            stateFromEnd = (row, col)
            
            if stateFromStart in distFromStart and stateFromEnd in distFromEnd:
                if distFromStart[stateFromStart] + distFromEnd[stateFromEnd] == optimal:
                    result.add((row, col))
    
    return result

def partOne():
    answer = 0
    
    start, end = generateInput()
    
    startRow, startCol = start
    endRow, endCol = end
    
    distFromStart = Dijkstra(startRow, startCol)
    distFromEnd = Dijkstra(endRow, endCol)
    
    normalTime = distFromStart[(endRow, endCol)]
    
    for i in range(1, len(map) - 1):
        for j in range(1, len(map[i]) - 1):
            if map[i][j] == Cell.Wall:
                map[i][j] = Cell.Empty
                
                newTime = 1_000_000_000_000
                
                for dir1 in Dir:
                    x1, y1 = dir1.value
                    
                    x1 = i + x1
                    y1 = j + y1
                    
                    for dir2 in Dir:
                        x2, y2 = dir2.value
                    
                        x2 = i + x2
                        y2 = j + y2
                        
                        if (x1, y1) in distFromStart and (x2, y2) in distFromEnd:
                            test = distFromStart[(x1, y1)] + distFromEnd[(x2, y2)] + 2
                            
                            if newTime > test:
                                newTime = test
                    
                
                if normalTime - newTime > 99:
                    answer += 1
                    
                map[i][j] = Cell.Wall
    
    return answer

def partTwo():
    answer = 0
    
    start, end = generateInput()
    
    startRow, startCol = start
    endRow, endCol = end
    
    distFromStart = Dijkstra(startRow, startCol)
    distFromEnd = Dijkstra(endRow, endCol)
    
    normalTime = distFromStart[(endRow, endCol)]
    
    path = getOptimalPath(distFromStart, distFromEnd, normalTime)
    
    for startCell in path:
        for endCell in path:            
            if distFromStart[startCell] < distFromStart[endCell]:
                man = manhattan(startCell, endCell)
                
                if man < 21:
                    newTime = distFromStart[startCell] + distFromEnd[endCell] + man
                    
                    if normalTime - newTime > 99:
                        answer += 1
    
    return answer

if __name__ == "__main__":    
    print(f'The answer for part one is: {partOne()}')
    print(f'The answer for part two is: {partTwo()}')