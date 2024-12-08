from enum import Enum, auto

lines = []

class Operation(Enum):
    Sum = auto(),
    Mul = auto(),
    Con = auto()
    
def concat(a, b):
    return int(f"{a}{b}")
    
def generateLines():
    
    lines.clear()
    
    with open('./2024/07/input.txt', 'r') as file:
        for line in file:
            l = line.split(':')
            l = l + l[1].split()
            l.pop(1)
            l = [int(x) for x in l]
            lines.append(l)
    
    return

def checkEq(testValue, line):
    valid = False
    
    valueTillThisPoint = line.pop(0)
    
    if resultOp(testValue, valueTillThisPoint, line.copy(), Operation.Sum) or resultOp(testValue, valueTillThisPoint, line.copy(), Operation.Mul):
        valid = True
    
    return valid

def checkEqCon(testValue, line):
    valid = False
    
    valueTillThisPoint = line.pop(0)
    
    if resultOpCon(testValue, valueTillThisPoint, line.copy(), Operation.Sum) or resultOpCon(testValue, valueTillThisPoint, line.copy(), Operation.Mul) or resultOpCon(testValue, valueTillThisPoint, line.copy(), Operation.Con):
        valid = True
    
    return valid

def resultOp(testValue, valueTillThisPoint, line, operation):
    
    if len(line) == 0:
        return testValue == valueTillThisPoint
    
    num = line.pop(0)
    
    if operation == Operation.Sum:
        valueTillThisPoint += num
    else:
        valueTillThisPoint *= num
    
    return resultOp(testValue, valueTillThisPoint, line.copy(), Operation.Sum) or resultOp(testValue, valueTillThisPoint, line.copy(), Operation.Mul)

def resultOpCon(testValue, valueTillThisPoint, line, operation):
    
    if len(line) == 0:
        return testValue == valueTillThisPoint
    
    num = line.pop(0)
    
    if operation == Operation.Sum:
        valueTillThisPoint += num
    elif operation == Operation.Mul:
        valueTillThisPoint *= num
    else:
        valueTillThisPoint = concat(valueTillThisPoint, num)
    
    return resultOpCon(testValue, valueTillThisPoint, line.copy(), Operation.Sum) or resultOpCon(testValue, valueTillThisPoint, line.copy(), Operation.Mul) or resultOpCon(testValue, valueTillThisPoint, line.copy(), Operation.Con)

def partOne():
    answer = 0
    
    generateLines() 

    for line in lines:
        testValue = line.pop(0)
        
        if checkEq(testValue, line):
            answer += testValue
    
    return answer

def partTwo():
    answer = 0
    
    generateLines()
    
    for line in lines:
        testValue = line.pop(0)
        
        if checkEqCon(testValue, line):
            answer += testValue
    
    return answer


if __name__ == "__main__":
    
    print(f'The answer for part one is: {partOne()}')
    print(f'The answer for part two is: {partTwo()}')