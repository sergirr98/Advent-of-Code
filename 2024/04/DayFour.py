lines = []

def partOne():
    answer = 0
    
    for i in range(len(lines)):
        for j in range(len(line)):
            if lines[i][j] == 'X':
                if (checkN(i, j)):
                    answer += 1
                if (checkNE(i, j)):
                    answer += 1
                if (checkE(i, j)):
                    answer += 1
                if (checkSE(i, j)):
                    answer += 1
                if (checkS(i, j)):
                    answer += 1
                if (checkSW(i, j)):
                    answer += 1
                if (checkW(i, j)):
                    answer += 1
                if (checkNW(i, j)):
                    answer += 1
    
    return answer

def checkN(i, j):
    check = False
    
    if (i > 2):
        if lines[i - 1][j] == 'M' and lines[i - 2][j] == 'A' and lines[i - 3][j] == 'S':
            check = True
    
    return check

def checkNE(i, j):
    check = False
    
    if (i > 2 and j < len(lines[i]) - 3):
        if lines[i - 1][j + 1] == 'M' and lines[i - 2][j + 2] == 'A' and lines[i - 3][j + 3] == 'S':
            check = True
    
    return check

def checkE(i, j):
    check = False
    
    if (j < len(lines[i]) - 3):
        if lines[i][j + 1] == 'M' and lines[i][j + 2] == 'A' and lines[i][j + 3] == 'S':
            check = True
    
    return check

def checkSE(i, j):
    check = False
    
    if (i < len(lines) - 3 and j < len(lines[i]) - 3):
        if lines[i + 1][j + 1] == 'M' and lines[i + 2][j + 2] == 'A' and lines[i + 3][j + 3] == 'S':
            check = True
    
    return check

def checkS(i, j):
    check = False
    
    if (i < len(lines) - 3):
        if lines[i + 1][j] == 'M' and lines[i + 2][j] == 'A' and lines[i + 3][j] == 'S':
            check = True
    
    return check

def checkSW(i, j):
    check = False
    
    if (i < len(lines) - 3 and j > 2):
        if lines[i + 1][j - 1] == 'M' and lines[i + 2][j - 2] == 'A' and lines[i + 3][j - 3] == 'S':
            check = True
    
    return check

def checkW(i, j):
    check = False
    
    if (j > 2):
        if lines[i][j - 1] == 'M' and lines[i][j - 2] == 'A' and lines[i][j - 3] == 'S':
            check = True
    
    return check

def checkNW(i, j):
    check = False
    
    if (i > 2 and j > 2):
        if lines[i - 1][j - 1] == 'M' and lines[i - 2][j - 2] == 'A' and lines[i - 3][j - 3] == 'S':
            check = True
    
    return check

def partTwo():
    answer = 0
    
    for i in range(len(lines)):
        for j in range(len(line)):
            if lines[i][j] == 'A':
                if (checkCross(i, j)):
                    answer += 1
    
    return answer

def checkCross(i ,j):
    check = False
    
    if (i > 0 and i < len(lines) - 1 and j > 0 and j < len(lines[i]) - 1):
        crossOne = lines[i - 1][j - 1] + lines[i + 1][j + 1]
        crossTwo = lines[i - 1][j + 1] + lines[i + 1][j - 1]
        
        if ((crossOne == "MS" or crossOne == "SM") and (crossTwo == "MS" or crossTwo == "SM")):
            check = True
    
    return check

if __name__ == "__main__":
    
    with open('./2024/04/input.txt', 'r') as file:
        for line in file:
            lines.append(line)
    
    print(f'The answer for part one is: {partOne()}')
    print(f'The answer for part two is: {partTwo()}')