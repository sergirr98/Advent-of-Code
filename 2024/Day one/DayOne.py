from time import perf_counter

leftList = []

rightList = []

def partOne():
    answer = 0
    
    leftList.sort()
    rightList.sort()
    
    for i in range(len(leftList)):
        answer += abs(leftList[i] - rightList[i])
    
    return answer

def partTwo():
    answer = 0
    
    for i in range(len(leftList)):
        elem = leftList[i]
        
        answer += elem * rightList.count(elem)
    
    return answer

def partTwoDict():
    answer = 0
    answerDict = dict()
    
    for elem in rightList:
        if elem in answerDict:
            answerDict[elem] += 1
        else:
            answerDict[elem] = 1
            
    for elem in leftList:
        if elem in answerDict:
            answer += elem * answerDict[elem]
    
    return answer

if __name__ == "__main__":
    
    with open('./2024/Day one/input.txt', 'r') as file:
        for line in file:
            l, r = line.split()
            l, r = int(l), int(r)
            leftList.append(l)
            rightList.append(r)
    
    print(partOne())
    
    # startTime = perf_counter()
    print(partTwo())
    # stopTime = perf_counter()
    
    # print(stopTime - startTime)
    
    # startTime = perf_counter()
    print(partTwoDict())
    # stopTime = perf_counter()
    
    # print(stopTime - startTime)