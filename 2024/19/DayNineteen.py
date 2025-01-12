towels = []
designs = []

def generateInput():
    isTowels = True
    
    with open('./2024/19/input.txt', 'r') as file:
        for line in file:
            if line == '\n':
                isTowels = False
                continue
            
            if isTowels:
                towelPatterns = line.split(', ')
                towelPatterns[-1] = towelPatterns[-1].replace('\n', '')
                towels.extend(towelPatterns)
            else:
                designs.append(line.replace('\n', ''))

def isOkay(design, memo):
    if design == "":
        return True
    
    if design in memo:
        return memo[design]
    
    memo[design] = False
    
    for towel in towels:
        length = len(towel)
        start = design[:length]
        rest = design[length:]
        
        if start == towel and isOkay(rest, memo):
            memo[design] = True
            
    return memo[design]

def isOkayTwo(design, memo):
    if design == "":
        return 1
    
    if design in memo:
        return memo[design]
    
    memo[design] = 0
    
    for towel in towels:
        length = len(towel)
        start = design[:length]
        rest = design[length:]
        
        if start == towel:
            memo[design] += isOkayTwo(rest, memo)
            
    return memo[design]

def isPossible(design):
    memo = dict()
    return isOkay(design, memo)

def isPossibleTwo(design):
    memo = dict()
    return isOkayTwo(design, memo)
    
def partOne():
    answer = 0
    
    for design in designs:
        if isPossible(design):
            answer += 1
    
    return answer

def partTwo():
    answer = 0
    
    for design in designs:
        answer += isPossibleTwo(design)
            
    return answer

if __name__ == "__main__":
    
    generateInput()
    
    print(f'The answer for part one is: {partOne()}')
    print(f'The answer for part two is: {partTwo()}')