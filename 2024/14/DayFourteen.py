import re
import statistics

rows = 103
cols = 101

robots = []

def generateInput():
    robots.clear()
    
    with open('./2024/14/input.txt', 'r') as file:
        for line in file:            
            numbers = re.findall(r'[-]?\d+', line)
            numbers = [int(x) for x in numbers]
            
            robot = []
            
            robot.append((numbers[0], numbers[1]))
            robot.append((numbers[2], numbers[3]))
            
            robots.append(robot)

def step(i, robot):
    currentPosX, currentPosY = robot[0]
    velX, velY = robot[1]
    
    currentPosX += velX
    currentPosY += velY
    
    if currentPosX < 0:
        currentPosX += cols
    elif currentPosX >= cols:
        currentPosX -= cols
        
    if currentPosY < 0:
        currentPosY += rows
    elif currentPosY >= rows:
        currentPosY -= rows
        
    robots[i] = [(currentPosX, currentPosY), (velX, velY)]

def moveRobots():
    for i, robot in enumerate(robots):
        step(i, robot)

def partOne():
    quadrantOne = 0
    quadrantTwo = 0
    quadrantThree = 0
    quadrantFour = 0
    
    for i in range(100):
        moveRobots()
        
    for robot in robots:
        currentPosX, currentPosY = robot[0]
        
        if currentPosX < cols // 2 and currentPosY < rows // 2:
            quadrantOne += 1
        elif currentPosX > cols // 2 and currentPosY < rows // 2:
            quadrantTwo += 1
        elif currentPosX > cols // 2 and currentPosY > rows // 2:
            quadrantThree += 1
        elif currentPosX < cols // 2 and currentPosY > rows // 2:
            quadrantFour += 1
    
    answer = quadrantOne * quadrantTwo * quadrantThree * quadrantFour
    
    return answer

def partTwo():
    
    generateInput()
    
    answer = 0
    
    while True:
        xPos = []
        yPos = []
        
        for robot in robots:            
            x, y = robot[0]
            
            xPos.append(x)
            yPos.append(y)

        xDev = statistics.stdev(xPos)
        yDev = statistics.stdev(yPos)
        
        # The 40 is an arbitrary number I decied on after testing AKA I pulled it out of my ass idk if it works on other inputs
        if xDev + yDev < 40:
            break
        
        moveRobots()
        answer += 1
        
    return answer

if __name__ == "__main__":
    
    generateInput()
    
    print(f'The answer for part one is: {partOne()}')
    print(f'The answer for part two is: {partTwo()}')