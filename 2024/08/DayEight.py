lines = []

mapLength = 49

def calculatePositionAntiNodes(posAntenaOne, posAntenaTwo):
    
    result = []
    
    antenaOneX, antenaOneY = posAntenaOne
    antenaTwoX, antenaTwoY = posAntenaTwo
    
    movX = antenaTwoX - antenaOneX
    movY = antenaTwoY - antenaOneY
    
    antiNodeOne = (antenaTwoX + movX, antenaTwoY + movY)
    antiNodeTwo = (antenaOneX - movX, antenaOneY - movY)
    
    if not (antiNodeOne[0] < 0 or antiNodeOne[0] > mapLength or antiNodeOne[1] < 0 or antiNodeOne[1] > mapLength):
        result.append(antiNodeOne)
    
    if not (antiNodeTwo[0] < 0 or antiNodeTwo[0] > mapLength or antiNodeTwo[1] < 0 or antiNodeTwo[1] > mapLength):
        result.append(antiNodeTwo)
    
    return result

def calculatePositionAntiNodesPartTwo(posAntenaOne, posAntenaTwo):
    
    result = []
        
    result.append(posAntenaOne)
    result.append(posAntenaTwo)
    
    antenaOneX, antenaOneY = posAntenaOne
    antenaTwoX, antenaTwoY = posAntenaTwo
    
    movX = antenaTwoX - antenaOneX
    movY = antenaTwoY - antenaOneY
    
    antiNodeOne = (antenaTwoX, antenaTwoY)
    antiNodeTwo = (antenaOneX, antenaOneY)
    
    while True:
        antiNodeOne = (antiNodeOne[0] + movX, antiNodeOne[1] + movY)
    
        if antiNodeOne[0] < 0 or antiNodeOne[0] > mapLength or antiNodeOne[1] < 0 or antiNodeOne[1] > mapLength:
            break
        
        result.append(antiNodeOne)
    
    while True:
        antiNodeTwo = (antiNodeTwo[0] - movX, antiNodeTwo[1] - movY)
        
        if antiNodeTwo[0] < 0 or antiNodeTwo[0] > mapLength or antiNodeTwo[1] < 0 or antiNodeTwo[1] > mapLength:
            break
        
        result.append(antiNodeTwo)
    
    return result

def calculateAntiNodes(elems):
    antiNodes = []
    
    for i in range(len(elems) - 1):
        for j in range(i + 1, len(elems)):
            antiNodes += calculatePositionAntiNodes(elems[i], elems[j])
    
    return antiNodes

def calculateAntiNodesPartTwo(elems):
    antiNodes = []
    
    for i in range(len(elems) - 1):
        for j in range(i + 1, len(elems)):
            antiNodes += calculatePositionAntiNodesPartTwo(elems[i], elems[j])
    
    return antiNodes

def partOne():
    answer = 0
    
    frequenciesPositions = dict()
    frequenciesChecked = set()
    
    for l_index, line in enumerate(lines):
        for c_index, char in enumerate(line):
            if char != '.':
                if not char in frequenciesPositions:
                    frequenciesPositions[char] = []
                
                frequenciesPositions[char].append((l_index, c_index))
                
    for key in frequenciesPositions:
        antiNodes = calculateAntiNodes(frequenciesPositions[key])
        
        for anti in antiNodes:
            frequenciesChecked.add(anti)
        
    answer = len(frequenciesChecked)
    
    return answer

def partTwo():
    
    answer = 0
    
    frequenciesPositions = dict()
    frequenciesChecked = set()
    
    for l_index, line in enumerate(lines):
        for c_index, char in enumerate(line):
            if char != '.':
                if not char in frequenciesPositions:
                    frequenciesPositions[char] = []
                
                frequenciesPositions[char].append((l_index, c_index))
                
    for key in frequenciesPositions:        
        antiNodes = calculateAntiNodesPartTwo(frequenciesPositions[key])
        
        for anti in antiNodes:
            frequenciesChecked.add(anti)
        
    answer = len(frequenciesChecked)
    
    return answer

if __name__ == "__main__":
    
    with open('./2024/08/input.txt', 'r') as file:
        raw = file.read()
        
        rawSplit = raw.split("\n")
        
        for line in rawSplit:
            lines.append(list(line))
    
    print(f'The answer for part one is: {partOne()}')
    print(f'The answer for part two is: {partTwo()}')