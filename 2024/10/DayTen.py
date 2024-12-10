from enum import Enum

class Dir(Enum):
    UP = -1, 0,
    RIGHT = 0, 1,
    DOWN = 1, 0,
    LEFT = 0, -1

map = []

def getNextStep(row, col, dir, expectedHeight, visitedPeaks, partTwo):
    rMov, cMov = dir.value
    
    row += rMov
    col += cMov
    
    if row < 0 or row > len(map) - 1 or col < 0 or col > len(map[row]) - 1:
        return 0
    
    if map[row][col] != expectedHeight:
        return 0
    
    if map[row][col] == 9:
        if (row, col) not in visitedPeaks or partTwo:
            visitedPeaks.add((row, col))
            return 1
        
        return 0

    expectedHeight += 1
    
    return getNextStep(row, col, Dir.UP, expectedHeight, visitedPeaks, partTwo) + getNextStep(row, col, Dir.RIGHT, expectedHeight, visitedPeaks, partTwo) + getNextStep(row, col, Dir.DOWN, expectedHeight, visitedPeaks, partTwo) + getNextStep(row, col, Dir.LEFT, expectedHeight, visitedPeaks, partTwo)
    
def getScore(row, col, partTwo):
    score = 0
    
    visitedPeaks = set()
        
    score = getNextStep(row, col, Dir.UP, 1, visitedPeaks, partTwo) + getNextStep(row, col, Dir.RIGHT, 1, visitedPeaks, partTwo) + getNextStep(row, col, Dir.DOWN, 1, visitedPeaks, partTwo) + getNextStep(row, col, Dir.LEFT, 1, visitedPeaks, partTwo)
    
    return score

def partOne():
    answer = 0
    
    for i, line in enumerate(map):
        for j, num in enumerate(line):
            if num == 0:
                answer += getScore(i, j, False)
    
    return answer

def partTwo():
    answer = 0
    
    for i, line in enumerate(map):
        for j, num in enumerate(line):
            if num == 0:
                answer += getScore(i, j, True)
    
    return answer

if __name__ == "__main__":
    
    with open('./2024/10/input.txt', 'r') as file:
        for line in file:
            mapLine = []
            for elem in line:
                if elem != "\n":
                    mapLine.append(elem)
                    
            mapLine = [int(x) for x in mapLine]
            map.append(mapLine)
    
    print(f'The answer for part one is: {partOne()}')
    print(f'The answer for part two is: {partTwo()}')