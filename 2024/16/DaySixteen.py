from enum import Enum, auto
import heapq

class Dir(Enum):
    UP = -1, 0
    RIGHT = 0, 1
    DOWN = 1, 0
    LEFT = 0, -1
    
    def __lt__(self, other):
        return self.value < other.value
    
    def flip(self):
        if self == Dir.UP:
            return Dir.DOWN
        
        if self == Dir.DOWN:
            return Dir.UP
        
        if self == Dir.RIGHT:
            return Dir.LEFT
        
        if self == Dir.LEFT:
            return Dir.RIGHT

class Cell(Enum):
    Empty = auto()
    Wall = auto()
    Start = auto()
    End = auto()
    
map = []

maxInt = 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000

stepScore = 1
turnScore = 1000

def generateMap():
    map.clear()
    
    startingRow = 0
    startingCol = 0
    
    endRow = 0
    endCol = 0
    
    with open('./2024/16/input.txt', 'r') as file:
            for i, line in enumerate(file):
                
                mapLine = []
                
                for j, elem in enumerate(line):
                    if elem == '\n':
                        continue
                    
                    if elem == '#':
                        mapLine.append(Cell.Wall)
                    elif elem == '.':
                        mapLine.append(Cell.Empty)
                    elif elem == 'S':
                        mapLine.append(Cell.Start)
                        
                        startingRow = i
                        startingCol = j
                    elif elem == 'E':
                        mapLine.append(Cell.End)
                        
                        endRow = i
                        endCol = j
                        
                map.append(mapLine)
                
    return startingRow, startingCol, endRow, endCol
                
def printMap():
    for line in map:
        for elem in line:
            if elem == Cell.Empty:
                print('.', end='')
            elif elem == Cell.Wall:
                print('#', end='')
            elif elem == Cell.Start:
                print('S', end='')
            elif elem == Cell.End:
                print('E', end='')

        print()

def Dijkstra(startingRow, strartingCol, startingDirs):
    
    dist = {}
    pq = []
    
    for dir in startingDirs:
        dist[(startingRow, strartingCol, dir)] = 0
        heapq.heappush(pq, (0, startingRow, strartingCol, dir))
    
    while pq:
        (d, row, col, dir) = heapq.heappop(pq)
        
        if dist[(row, col, dir)] < d:
            continue
        
        for nextDir in Dir:
            if nextDir != dir:
                if (row, col, nextDir) not in dist or dist[(row, col, nextDir)] > d + turnScore:
                    nextD = d + turnScore
                    dist[(row, col, nextDir)] = nextD
                    heapq.heappush(pq, (nextD, row, col, nextDir))
                
        dRow, dCol = dir.value
        
        nextRow = row + dRow
        nextCol = col + dCol
        
        if (0 <= nextRow < len(map) and 0 <= nextCol < len(map[0])) and map[nextRow][nextCol] != Cell.Wall and ((nextRow, nextCol, dir) not in dist or dist[(nextRow, nextCol, dir)] > d + stepScore):
            nextS = d + stepScore
            dist[(nextRow, nextCol, dir)] = nextS
            heapq.heappush(pq, (nextS, nextRow, nextCol,dir))
    
    return dist

# HEAVILY inspired by reddit
def partOne():
    answer = maxInt
    
    startingRow, startingCol, endRow, endCol = generateMap()
    
    dist = Dijkstra(startingRow, startingCol, [Dir.RIGHT])
    
    for dir in Dir:
        if (endRow, endCol, dir) in dist:
            answer = min(answer, dist[(endRow, endCol, dir)])
    
    return answer

def partTwo():
    answer = 0
    
    startingRow, startingCol, endRow, endCol = generateMap()
    
    distStart = Dijkstra(startingRow, startingCol, [Dir.RIGHT])
    distEnd = Dijkstra(endRow, endCol, [Dir.UP, Dir.RIGHT, Dir.DOWN, Dir.LEFT])
    
    optimal = partOne()
    
    result = set()
    
    for row in range(len(map)):
        for col in range(len(map[row])):
            for dir in Dir:
                stateFromStart = (row, col, dir)
                stateFromEnd = (row, col, dir.flip())
                
                if stateFromStart in distStart and stateFromEnd in distEnd:
                    if distStart[stateFromStart] + distEnd[stateFromEnd] == optimal:
                        result.add((row, col))
    
    answer = len(result)
    
    return answer

if __name__ == "__main__":
    print(f'The answer for part one is: {partOne()}')
    print(f'The answer for part two is: {partTwo()}')