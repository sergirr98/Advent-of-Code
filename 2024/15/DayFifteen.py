from enum import Enum, auto

class Dir(Enum):
    UP = -1, 0
    RIGHT = 0, 1
    DOWN = 1, 0
    LEFT = 0, -1
    
class Map(Enum):
    Empty = auto()
    Player = auto()
    Wall = auto()
    Box = auto()
    BoxLeft = auto()
    BoxRight = auto()
    
map = []
movements = []

def generateMap():
    map.clear()
    movements.clear()
    
    firstPart = True
    
    startingPos = ()
    
    with open('./2024/15/input.txt', 'r') as file:
            for i, line in enumerate(file):
                if line == "\n":
                    firstPart = False
                    continue
                
                if firstPart:
                
                    mapLine = []
                    for j, elem in enumerate(line):
                        if elem == '\n':
                            continue
                        if elem == '#':
                            mapLine.append(Map.Wall)
                        elif elem == '.':
                            mapLine.append(Map.Empty)
                        elif elem == 'O':
                            mapLine.append(Map.Box)
                        else:
                            mapLine.append(Map.Player)
                            startingPos = (i, j)
                            
                    map.append(mapLine)
                
                else:
                    for elem in line:
                        if elem == '\n':
                            continue
                        
                        if elem == '^':
                            movements.append(Dir.UP)
                        elif elem == '>':
                            movements.append(Dir.RIGHT)
                        elif elem == 'v':
                            movements.append(Dir.DOWN)
                        else:
                            movements.append(Dir.LEFT)

    return startingPos

def generateMapTwo():
    map.clear()
    movements.clear()
    
    firstPart = True
    
    startingPos = ()
    
    with open('./2024/15/input.txt', 'r') as file:
            for i, line in enumerate(file):
                if line == "\n":
                    firstPart = False
                    continue
                
                if firstPart:
                
                    mapLine = []
                    for j, elem in enumerate(line):
                        if elem == '\n':
                            continue
                        if elem == '#':
                            mapLine.append(Map.Wall)
                            mapLine.append(Map.Wall)
                        elif elem == '.':
                            mapLine.append(Map.Empty)
                            mapLine.append(Map.Empty)
                        elif elem == 'O':
                            mapLine.append(Map.BoxLeft)
                            mapLine.append(Map.BoxRight)
                        else:
                            mapLine.append(Map.Player)
                            mapLine.append(Map.Empty)
                            startingPos = (i, j * 2)
                            
                    map.append(mapLine)
                
                else:
                    for elem in line:
                        if elem == '\n':
                            continue
                        
                        if elem == '^':
                            movements.append(Dir.UP)
                        elif elem == '>':
                            movements.append(Dir.RIGHT)
                        elif elem == 'v':
                            movements.append(Dir.DOWN)
                        else:
                            movements.append(Dir.LEFT)

    return startingPos

def printMap():
    for line in map:
        for elem in line:
            if elem == Map.Box:
                print('O', end='')
            elif elem == Map.BoxLeft:
                print('[', end='')
            elif elem == Map.BoxRight:
                print(']', end='')
            elif elem == Map.Empty:
                print('.', end='')
            elif elem == Map.Wall:
                print('#', end='')
            else:
                print('@', end='')
        print()

def checkDirection(dir, pos):
    canMove = False
    
    dirX, dirY = dir.value
    posX, posY = pos
    
    posX += dirX
    posY += dirY
    
    while True:
        if map[posX][posY] == Map.Wall:
            canMove = False
            break
        
        if map[posX][posY] == Map.Empty:
            canMove = True
            break
        
        posX += dirX
        posY += dirY
        
    return canMove   

def checkDirectionTwo(dir, pos, alreadyChecked):
    
    alreadyChecked.add(pos)
    
    canMove = True
    
    dirX, dirY = dir.value
    posX, posY = pos
    
    posX += dirX
    posY += dirY
    
    while True:
        if map[posX][posY] == Map.Wall:
            canMove = False
            break
        
        if map[posX][posY] == Map.Empty:
            canMove = canMove and True
            break
        
        if map[posX][posY] == Map.BoxLeft and (dir == Dir.UP or dir == Dir.DOWN):
            boxY = posY + 1
            if (posX, boxY) not in alreadyChecked:
                canMove = canMove and checkDirectionTwo(dir, (posX, boxY), alreadyChecked)
                
        if map[posX][posY] == Map.BoxRight and (dir == Dir.UP or dir == Dir.DOWN):
            boxY = posY - 1
            if (posX, boxY) not in alreadyChecked:
                canMove = canMove and checkDirectionTwo(dir, (posX, boxY), alreadyChecked)
        
        posX += dirX
        posY += dirY
        
    return canMove 

def moveElem(dir, pos, alreadyMoved):
    alreadyMoved.add(pos)
    
    dirX, dirY = dir.value
    posX, posY = pos
    
    nextPosX = posX + dirX
    nextPosY = posY + dirY
    
    if map[nextPosX][nextPosY] != Map.Empty:
        moveElem(dir, (nextPosX, nextPosY), alreadyMoved)
        
    if map[posX][posY] == Map.BoxLeft and (dir == Dir.UP or dir == Dir.DOWN):
        boxY = posY + 1
        if (posX, boxY) not in alreadyMoved:
            moveElem(dir, (posX, boxY), alreadyMoved)
                
    if map[posX][posY] == Map.BoxRight and (dir == Dir.UP or dir == Dir.DOWN):
        boxY = posY - 1
        if (posX, boxY) not in alreadyMoved:
            moveElem(dir, (posX, boxY), alreadyMoved)
            
    map[nextPosX][nextPosY] = map[posX][posY]
    map[posX][posY] = Map.Empty
    
    return (nextPosX, nextPosY)
        

def step(move, pos):
    canMove = checkDirection(move, pos)
    
    if not canMove:
        return pos
    
    dirX, dirY = move.value
    posX, posY = pos
    
    heldElem = Map.Player
    map[posX][posY] = Map.Empty
    
    posX += dirX
    posY += dirY
    
    newPos = (posX, posY)
    
    while True:
        if map[posX][posY] == Map.Empty:
            map[posX][posY] = heldElem
            break 
        
        map[posX][posY] = heldElem
        heldElem = Map.Box
        
        posX += dirX
        posY += dirY
    
    return newPos

def stepTwo(move, pos):
    alreadyChecked = set()
    
    canMove = checkDirectionTwo(move, pos, alreadyChecked)
    
    if not canMove:
        return pos
    
    alreadyMoved = set()
    
    newPos = moveElem(move, pos, alreadyMoved)
        
    return newPos

def simulate(startingPos):
    
    pos = startingPos
    
    for move in movements:
        newPos = step(move, pos)
        pos = newPos

def simulateTwo(startingPos):
    
    pos = startingPos
    
    for move in movements:
        newPos = stepTwo(move, pos)
        pos = newPos

def calculateGPS():
    totalGPS = 0
    
    for i, line in enumerate(map):
        for j, elem in enumerate(line):
            if elem == Map.Box:
                totalGPS += i * 100 + j
                
    return totalGPS

def calculateGPSTwo():
    totalGPS = 0
    
    for i, line in enumerate(map):
        for j, elem in enumerate(line):
            if elem == Map.BoxLeft:
                totalGPS += i * 100 + j
                
    return totalGPS

def partOne():
    answer = 0
    
    startingPos = generateMap()
    
    simulate(startingPos)
    
    answer = calculateGPS()
    
    return answer

def partTwo():
    answer = 0
    
    startingPos = generateMapTwo()
    
    simulateTwo(startingPos)
    
    answer = calculateGPSTwo()
    
    return answer
    
if __name__ == "__main__":     
    print(f'The answer for part one is: {partOne()}')
    print(f'The answer for part two is: {partTwo()}')