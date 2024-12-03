listOfLines = []

def partOne():
    answer = 0
    
    for line in listOfLines:
        if checkValidity(line) == -1:
            answer += 1
    
    return answer

def partTwo():
    answer = 0
    
    for line in listOfLines:
        
        index = checkValidity(line)
        
        if index == -1:
            answer += 1
        else:
            
            testOne = line.copy()
            testTwo = line.copy()
            
            testOne.pop(index)
            testTwo.pop(index + 1)
            
            if checkValidity(testOne) == -1 or checkValidity(testTwo) == -1:
                answer += 1
            elif index > 0:
                testThree = line.copy()
                testThree.pop(index - 1)
                
                if checkValidity(testThree) == -1:
                    answer += 1
                
    return answer

def checkValidity(line):
    check = -1
    
    asc = False
    des = False
    
    for i in range(len(line) - 1):
        a = line[i]
        b = line[i + 1]
        
        if a < b:
            asc = True
        elif a > b:
            des = True
        else:
            asc = True
            des = True
        
        if asc and des:
            check = i
            break
        
        if abs(a - b) > 3:
            check = i
            break
        
    return check

if __name__ == "__main__":
    
    with open('./2024/Day two/input.txt', 'r') as file:
        for line in file:
            l = line.split()
            l = [int(x) for x in l]
            listOfLines.append(l)
    
    print(f'The answer for part one is: {partOne()}')
    print(f'The answer for part two is: {partTwo()}')