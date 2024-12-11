from time import perf_counter

nums = []

def generateStones():
    stones = []
    
    with open('./2024/11/input.txt', 'r') as file:
        for line in file:
            numLine = line.split()
            stones = [int(x) for x in numLine] 
            
    return stones

def getNumLength(num):
    return len(str(num))

def splitNum(num):
    sNum = str(num)
    
    left = sNum[:len(sNum) // 2]
    right = sNum[len(sNum) // 2:]
    
    return int(left), int(right)

def splitRock(stone):
    
    left, right = splitNum(stone)
    
    return left, right

def transformRock(stone):
    
    if stone == 0:
        return [1]
    
    elif getNumLength(stone) % 2 == 0:
        left, right = splitRock(stone)
        return [left, right]
    
    else:
        return [stone * 2024]

def partOne():
    answer = 0
    
    stones = generateStones()
    
    for i in range(25):
        newStones = []
        
        for stone in stones:
            newStones += transformRock(stone)

        stones = newStones
    
    answer = len(stones)
    
    return answer

def partTwo():
    answer = 0
    
    stones = generateStones()
    stoneDict = dict()
    
    for stone in stones:
        if not stone in stoneDict:
            stoneDict[stone] = 0
        
        stoneDict[stone] += 1
    
    for i in range(75):
        newStonesDict = dict()
        
        for stone in stoneDict:
            newStones = transformRock(stone)
            
            for newStone in newStones:
                if not newStone in newStonesDict:
                    newStonesDict[newStone] = 0
                
                newStonesDict[newStone] += stoneDict[stone]
        
        stoneDict = newStonesDict
    
    for key in stoneDict:
        answer += stoneDict[key]
    
    return answer

if __name__ == "__main__":
                
    print(f'The answer for part one is: {partOne()}')
    
    # startTime = perf_counter()
    print(f'The answer for part two is: {partTwo()}')
    # stopTime = perf_counter()
    
    # print(stopTime - startTime)