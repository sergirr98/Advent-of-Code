import re
from enum import Enum

class Button(Enum):
    A = 3
    B = 1
    
maxNum = 1_000_000_000_000_000_000_000_000

lines = []

lines2 = []

def generateInput():
    with open('./2024/13/input.txt', 'r') as file:
        counter = 0
        machine = []
        for line in file:
            if counter == 3:
                lines.append(machine)
                counter = 0
                machine = []
                continue
            
            numbers = re.findall(r'\d+', line)
            numbers = [int(x) for x in numbers]
            machine.append(tuple(numbers))
            counter += 1
    
    lines.append(machine)
    
def generateInput2():
    with open('./2024/13/input.txt', 'r') as file:
        counter = 0
        machine = []
        for line in file:
            if counter == 3:
                lines2.append(machine)
                counter = 0
                machine = []
                continue
            
            numbers = re.findall(r'\d+', line)
            numbers = [int(x) for x in numbers]
            
            if counter == 2:
                for i, num in enumerate(numbers):
                    numbers[i] = num + 10000000000000
            
            machine.append(tuple(numbers))
            counter += 1
    
    lines2.append(machine)

def getCheapPath(currentCost, machine, currentPos, button, posCost):       
    if button == Button.A:
        x, y = machine[0]
    else:
        x, y = machine[1]
    
    cPx, cPy = currentPos
    
    cPx += x
    cPy += y
    
    if cPx > machine[2][0] or cPy > machine[2][1]:
        return maxNum
    
    currentCost += button.value
    currentPos = (cPx, cPy)
    
    if currentPos in posCost:
        if posCost[currentPos] <= currentCost:
            return maxNum
        else:
            posCost[currentPos] = currentCost
    else:
        posCost[currentPos] = currentCost
    
    if currentPos == machine[2]:
        return currentCost
    
    return min(getCheapPath(currentCost, machine, currentPos, Button.A, posCost), getCheapPath(currentCost, machine, currentPos, Button.B, posCost))    

def getPathValue(machine, posCost):
    currentPos = (0, 0)
    
    pathA = getCheapPath(0, machine, currentPos, Button.A, posCost)
    pathB = getCheapPath(0, machine, currentPos, Button.B, posCost)
    
    return min(pathA, pathB)    

def partOne():
    generateInput()
    
    answer = 0
    
    for machine in lines:
        posCost = dict()
        value = getPathValue(machine, posCost)
        
        if value < maxNum:
            answer += value
    
    return answer

def partTwo():
    generateInput2()
    
    answer = 0
    
    for machine in lines2:
        buttonA = machine[0]
        buttonB = machine[1]
        finalPos = machine[2]
        
        pressesB = (buttonA[1] * finalPos[0] - buttonA[0] * finalPos[1]) / (buttonA[1] * buttonB[0] - buttonA[0] * buttonB[1])
        pressesA = (finalPos[1] - buttonB[1] * pressesB) / buttonA[1]
        
        if pressesA % 1 == 0 and pressesB % 1 == 0:
            answer += pressesA * Button.A.value + pressesB * Button.B.value
    
    return int(answer)

if __name__ == "__main__":
    print(f'The answer for part one is: {partOne()}')
    print(f'The answer for part two is: {partTwo()}')