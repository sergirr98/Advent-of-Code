from enum import Enum

class Dir(Enum):
    UP = -1, 0,
    RIGHT = 0, 1,
    DOWN = 1, 0,
    LEFT = 0, -1

garden = []

def getArea(row, col, plant, visitedPlants, dir):
    rMov, cMov = dir.value
    
    row += rMov
    col += cMov
    
    if row < 0 or row > len(garden) - 1 or col < 0 or col > len(garden[row]) - 1:
        return 0
    
    if garden[row][col] != plant:
        return 0
    
    if (row, col) in visitedPlants:
        return 0
    
    visitedPlants.add((row, col))
    
    return getArea(row, col, plant, visitedPlants, Dir.UP) + getArea(row, col, plant, visitedPlants, Dir.RIGHT) + getArea(row, col, plant, visitedPlants, Dir.DOWN) + getArea(row, col, plant, visitedPlants, Dir.LEFT) + 1

def getPeri(row, col, plant, visitedPlants, dir):
    rMov, cMov = dir.value
    
    row += rMov
    col += cMov
    
    if row < 0 or row > len(garden) - 1 or col < 0 or col > len(garden[row]) - 1:
        return 1
    
    if garden[row][col] != plant:
        return 1
    
    if (row, col) in visitedPlants:
        return 0
    
    visitedPlants.add((row, col))
    
    return getPeri(row, col, plant, visitedPlants, Dir.UP) + getPeri(row, col, plant, visitedPlants, Dir.RIGHT) + getPeri(row, col, plant, visitedPlants, Dir.DOWN) + getPeri(row, col, plant, visitedPlants, Dir.LEFT)

def getCorners(row, col, plant):
    corners = 0
    
    up = False
    upRight = False
    right = False
    downRight = False
    down = False
    downLeft = False
    left = False
    upLeft = False
        
    if row - 1 < 0 or row - 1 > len(garden) - 1 or col < 0 or col > len(garden[row - 1]) - 1 or garden[row - 1][col] != plant:
        up = True
    if row  < 0 or row > len(garden) - 1 or col + 1 < 0 or col + 1 > len(garden[row]) - 1 or garden[row][col + 1] != plant:
        right = True
    if row + 1  < 0 or row + 1 > len(garden) - 1 or col < 0 or col > len(garden[row + 1]) - 1 or garden[row + 1][col] != plant:
        down = True
    if row  < 0 or row > len(garden) - 1 or col - 1 < 0 or col - 1 > len(garden[row]) - 1 or garden[row][col - 1] != plant:
        left = True
    
    if row - 1 < 0 or row - 1 > len(garden) - 1 or col + 1 < 0 or col + 1 > len(garden[row - 1]) - 1 or garden[row - 1][col + 1] != plant:    
        upRight = True
    if row + 1 < 0 or row + 1 > len(garden) - 1 or col + 1 < 0 or col + 1 > len(garden[row + 1]) - 1 or garden[row + 1][col + 1] != plant:
        downRight = True
    if row + 1 < 0 or row + 1 > len(garden) - 1 or col - 1 < 0 or col - 1 > len(garden[row + 1]) - 1 or garden[row + 1][col - 1] != plant:
        downLeft = True
    if row - 1 < 0 or row - 1 > len(garden) - 1 or col - 1 < 0 or col - 1 > len(garden[row - 1]) - 1 or garden[row - 1][col - 1] != plant:
        upLeft = True
        
    if up and right:
        corners += 1
    if right and down:
        corners += 1
    if down and left:
        corners += 1
    if left and up:
        corners += 1
        
    if not up and not right and upRight:
        corners += 1
    if not right and not down and downRight:
        corners += 1
    if not down and not left and downLeft:
        corners += 1
    if not left and not up and upLeft:
        corners += 1
    
    return corners

def getPeriPartTwo(row, col, plant, visitedPlants, dir):
    rMov, cMov = dir.value
    
    row += rMov
    col += cMov
    
    if row < 0 or row > len(garden) - 1 or col < 0 or col > len(garden[row]) - 1:
        return 0
    
    if garden[row][col] != plant:
        return 0
    
    if (row, col) in visitedPlants:
        return 0
    
    visitedPlants.add((row, col))
    corners = getCorners(row, col, plant)
    
    return corners + getPeriPartTwo(row, col, plant, visitedPlants, Dir.UP) + getPeriPartTwo(row, col, plant, visitedPlants, Dir.RIGHT) + getPeriPartTwo(row, col, plant, visitedPlants, Dir.DOWN) + getPeriPartTwo(row, col, plant, visitedPlants, Dir.LEFT)

def getFenceCost(row, col, plant, visitedPlants):
    
    visitedPlants.add((row, col))
    visitedPlantsPeri = visitedPlants.copy()
    
    area = getArea(row, col, plant, visitedPlants, Dir.UP) + getArea(row, col, plant, visitedPlants, Dir.RIGHT) + getArea(row, col, plant, visitedPlants, Dir.DOWN) + getArea(row, col, plant, visitedPlants, Dir.LEFT) + 1
    
    peri = getPeri(row, col, plant, visitedPlantsPeri, Dir.UP) + getPeri(row, col, plant, visitedPlantsPeri, Dir.RIGHT) + getPeri(row, col, plant, visitedPlantsPeri, Dir.DOWN) + getPeri(row, col, plant, visitedPlantsPeri, Dir.LEFT)
    
    return area * peri

def getFenceCostPartTwo(row, col, plant, visitedPlants):
    
    visitedPlants.add((row, col))
    visitedPlantsPeri = visitedPlants.copy()
    
    sides = getCorners(row, col, plant)
    
    area = getArea(row, col, plant, visitedPlants, Dir.UP) + getArea(row, col, plant, visitedPlants, Dir.RIGHT) + getArea(row, col, plant, visitedPlants, Dir.DOWN) + getArea(row, col, plant, visitedPlants, Dir.LEFT) + 1
    
    sides += getPeriPartTwo(row, col, plant, visitedPlantsPeri, Dir.UP) + getPeriPartTwo(row, col, plant, visitedPlantsPeri, Dir.RIGHT) + getPeriPartTwo(row, col, plant, visitedPlantsPeri, Dir.DOWN) + getPeriPartTwo(row, col, plant, visitedPlantsPeri, Dir.LEFT)
    
    return area * sides

def partOne():
    answer = 0
    
    visitedPlants = set()
    
    for i, gardenLine in enumerate(garden):
        for j, plant in enumerate(gardenLine):
            if (i, j) not in visitedPlants:
                answer += getFenceCost(i, j, plant, visitedPlants)
    
    return answer

def partTwo():
    answer = 0
    
    visitedPlants = set()
    
    for i, gardenLine in enumerate(garden):
        for j, plant in enumerate(gardenLine):
            if (i, j) not in visitedPlants:
                answer += getFenceCostPartTwo(i, j, plant, visitedPlants)
    
    return answer

if __name__ == "__main__":
    with open('./2024/12/input.txt', 'r') as file:
            for line in file:
                gardenLine = []
                for elem in line:
                    if elem != "\n":
                        gardenLine.append(elem)
                        
                garden.append(gardenLine)
            
    print(f'The answer for part one is: {partOne()}')    
    print(f'The answer for part two is: {partTwo()}')