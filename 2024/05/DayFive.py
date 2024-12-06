rules = []
manuals = []

prevPagesDic = dict()
afterPagesDic = dict()

def partOne():
    answer = 0
    
    for line in manuals:
        if checkValidity(line):
            answer += getMiddle(line)
    
    return answer

def checkValidity(line):
    
    for i in range(1, len(line)):
        for j in range(i):
            if line[j] in prevPagesDic[line[i]]:
                return False
    
    return True

def getMiddle(line):
    return line[len(line) // 2]

def partTwo():
    answer = 0
    
    for line in manuals:
        if not checkValidity(line):
            newLine = moveAround(line)
            answer += getMiddle(newLine)
    
    return answer

def moveAround(line):
    newLine = list()
    newLine.append(line[0])
    
    added = False
    
    for i in range(1, len(line)):
        for j in range(len(newLine)):
            if (line[i] in afterPagesDic[newLine[j]]):
                newLine.insert(j, line[i])
                added = True
                break
        
        if not added:
            newLine.append(line[i])
        
        added = False

    return newLine

if __name__ == "__main__":   
    switch = True
    
    with open('./2024/05/input.txt', 'r') as file:
        for line in file:
            if len(line.strip()) == 0:
                switch = False
                continue
            
            if switch:
                l = line.split('|')
                l = [int(x) for x in l]
                rules.append(l)
                
            else:
                l = line.split(',')
                l = [int(x) for x in l]
                manuals.append(l)
                
    for line in rules:
        if not line[0] in prevPagesDic:
            prevPagesDic[line[0]] = list()
        
        prevPagesDic[line[0]].append(line[1])
        
    for line in rules:
        if not line[1] in afterPagesDic:
            afterPagesDic[line[1]] = list()
        
        afterPagesDic[line[1]].append(line[0])
    
    print(f'The answer for part one is: {partOne()}')
    print(f'The answer for part two is: {partTwo()}')