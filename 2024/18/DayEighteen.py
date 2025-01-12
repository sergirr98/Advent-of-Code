import re
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
    
    # def __lt__(self, other):
    #     return self.value < other.value

coords = []

rows = 71
cols = 71

map = []

def generateCoords():
    with open('./2024/18/input.txt', 'r') as file:
        for line in file:
            numbers = re.findall(r'[-]?\d+', line)
            numbers = [int(x) for x in numbers]
            
            coords.append(numbers)

def generateMap(bytes):
    for i in range(rows):
        line = []
        for j in range(cols):
            line.append(Cell.Empty)
        map.append(line)
    
    for i in range(bytes):
        x = coords[i][0]
        y = coords[i][1]
        
        map[y][x] = Cell.Wall

def addObstacle(i):
    x = coords[i][0]
    y = coords[i][1]
        
    map[y][x] = Cell.Wall

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

def partOne():
    
    generateCoords()
    generateMap(1024)
    
    dist = Dijkstra(0, 0)
    
    return dist[(70, 70)]

# Can be heavy optimized
def partTwo():
    index = 0
    
    for i in range(1024, len(coords)):
        addObstacle(i)
        dist = Dijkstra(0, 0)
        if (70, 70) not in dist:
            index = i
            break
    
    return ','.join(str(x) for x in coords[index])

if __name__ == "__main__":
    print(f'The answer for part one is: {partOne()}')
    print(f'The answer for part two is: {partTwo()}')