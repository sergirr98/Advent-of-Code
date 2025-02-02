import re
from enum import Enum
from queue import Queue

class Num(Enum):
    ZERO = 3, 1
    ONE = 2, 0
    TWO = 2, 1
    THREE = 2, 2
    FOUR = 1, 0
    FIVE = 1, 1
    SIX = 1, 2
    SEVEN = 0, 0
    EIGHT = 0, 1
    NINE = 0, 2
    A = 3, 2
    ERROR = 3, 0
    
    def getNum(string):
        if string == '0':
            return Num.ZERO
        if string == '1':
            return Num.ONE
        if string == '2':
            return Num.TWO
        if string == '3':
            return Num.THREE
        if string == '4':
            return Num.FOUR
        if string == '5':
            return Num.FIVE
        if string == '6':
            return Num.SIX
        if string == '7':
            return Num.SEVEN
        if string == '8':
            return Num.EIGHT
        if string == '9':
            return Num.NINE
        if string == 'A':
            return Num.A
    
class Arrow(Enum):
    UP = 0, 1
    DOWN = 1, 1
    LEFT = 1, 0
    RIGHT = 1, 2
    A = 0, 2
    ERROR = 0, 0
    
    def getKey(string):
        if string == '^':
            return Arrow.UP
        if string == 'v':
            return Arrow.DOWN
        if string == '<':
            return Arrow.LEFT
        if string == '>':
            return Arrow.RIGHT
        if string == 'A':
            return Arrow.A

codes = []

memo = dict()

BIG_NUM = 1_000_000_000_000_000_000_000_000_000_000_000_000

def generateInput():
    with open('./2024/21/input.txt', 'r') as file:
        for line in file:
            codes.append(line.replace('\n', ''))

def manhattan(start, end):
    startRow, startCol = start
    endRow, endCol = end
    
    return startRow - endRow, startCol - endCol

def processFirstRobot(code):
    
    start = Num.A.value
    
    row, col = start
    error = False
    
    moves = []
    
    for char in code:
        next = Num.getNum(char).value
        moveRow, moveCol = manhattan(start, next)
        
        moveLeftRigh = []
        moveUpDown = []
        error = False
        
        for i in range(abs(moveCol)):
            if moveCol > 0:
                moveLeftRigh.append('<')
                col -= 1
                
                if (row, col) == Num.ERROR.value:
                    error = True
        
        for i in range(abs(moveRow)):
            if moveRow < 0:
                moveUpDown.append('v')
                row += 1
                
                if (row, col) == Num.ERROR.value:
                    error = True
            else:
                moveUpDown.append('^')
                row -= 1 
                
                if (row, col) == Num.ERROR.value:
                    error = True
                    
        for i in range(abs(moveCol)):
            if moveCol < 0:
                moveLeftRigh.append('>')
                col += 1
                
                if (row, col) == Num.ERROR.value:
                    error = True
                    
        if moveCol > 0:
            if not error:
                moves.extend(moveLeftRigh)
                moves.extend(moveUpDown)
            else:
                moves.extend(moveUpDown)
                moves.extend(moveLeftRigh)
        else:
            if not error:
                moves.extend(moveUpDown)
                moves.extend(moveLeftRigh)
            else:
                moves.extend(moveLeftRigh)
                moves.extend(moveUpDown)
            
        moves.append('A')
        
        start = next
            
    return moves

def processOtherRobots(moves, movesAlreadyMade):
    start = Arrow.A.value
    
    row, col = start
    error = False
    
    newMoves = []
    
    for move in moves:
        next = Arrow.getKey(move).value
        
        if (start, next) in movesAlreadyMade:
            newMoves.extend(movesAlreadyMade[(start, next)])
        
        else:
        
            moveRow, moveCol = manhattan(start, next)
            
            moveLeftRigh = []
            moveUpDown = []
            error = False
            
            for i in range(abs(moveCol)):
                if moveCol > 0:
                    moveLeftRigh.append('<')
                    col -= 1
                    
                    if (row, col) == Arrow.ERROR.value:
                        error = True
            
            for i in range(abs(moveRow)):
                if moveRow < 0:
                    moveUpDown.append('v')
                    row += 1
                    
                    if (row, col) == Arrow.ERROR.value:
                        error = True
                else:
                    moveUpDown.append('^')
                    row -= 1 
                    
                    if (row, col) == Arrow.ERROR.value:
                        error = True
                        
            for i in range(abs(moveCol)):
                if moveCol < 0:
                    moveLeftRigh.append('>')
                    col += 1
                    
                    if (row, col) == Arrow.ERROR.value:
                        error = True
                        
            if moveCol > 0:
                if not error:
                    
                    aux = []
                    
                    aux.extend(moveLeftRigh)
                    aux.extend(moveUpDown)
                    
                    movesAlreadyMade[(start, next)] = aux 
                    
                    newMoves.extend(aux)
                else:
                    aux = []
                    
                    aux.extend(moveUpDown)
                    aux.extend(moveLeftRigh)
                    
                    movesAlreadyMade[(start, next)] = aux 
                    
                    newMoves.extend(aux)
            else:
                if not error:
                    aux = []
                    
                    aux.extend(moveUpDown)
                    aux.extend(moveLeftRigh)
                    
                    movesAlreadyMade[(start, next)] = aux 
                    
                    newMoves.extend(aux)
                else:
                    aux = []
                    
                    aux.extend(moveLeftRigh)
                    aux.extend(moveUpDown)
                    
                    movesAlreadyMade[(start, next)] = aux 
                    
                    newMoves.extend(aux)
            
        newMoves.append('A')
        
        start = next
        
    return newMoves

def shortestMoves(code, iterations):
    moves = processFirstRobot(code)
    
    movesAlreadyMade = dict()
    
    for i in range(iterations):
        moves = processOtherRobots(moves, movesAlreadyMade)
    
    return len(moves)

def numericPart(code):
    list = re.findall(r'\d+', code)
    
    return int(list[0])

def processCode(code, iterations):
    length = shortestMoves(code, iterations)
    num = numericPart(code)
    
    return length * num

def partOne():
    answer = 0
    
    generateInput()
    
    for code in codes:
        answer += processCode(code, 2)
    
    return answer

def cheapestDirPad(currentRow, currentCol, destRow, destCol, nRobot):
    
    if (currentRow, currentCol, destRow, destCol, nRobot) in memo:
        return memo[(currentRow, currentCol, destRow, destCol, nRobot)]
    
    answer = BIG_NUM
    
    q = Queue()
    
    q.put((currentRow, currentCol, ""))
    
    while not q.empty():
        row, col, presses = q.get()
        
        if (row, col) == (destRow, destCol):
            rec = cheapestRobot(presses + "A", nRobot - 1)
            answer = min(answer, rec)
            continue
        
        if (row, col) == Arrow.ERROR.value:
            continue
        
        else:
            if row < destRow:
                q.put((row + 1, col, presses + "v"))
            elif row > destRow:
                q.put((row - 1, col, presses + "^"))
                
            if col < destCol:
                q.put((row, col + 1, presses + ">"))
            elif col > destCol:
                q.put((row, col - 1, presses + "<"))
    
    memo[(currentRow, currentCol, destRow, destCol, nRobot)] = answer
    
    return answer

def cheapestRobot(presses, nRobot):
    
    if nRobot == 1:
        return len(presses)
    
    result = 0
    
    currentRow, currentCol = Arrow.A.value
    
    for char in presses:
        nextRow, nextCol = Arrow.getKey(char).value
        result += cheapestDirPad(currentRow, currentCol, nextRow, nextCol, nRobot)
        currentRow = nextRow
        currentCol = nextCol
    
    return result

def cheapest(currentRow, currentCol, destRow, destCol):
    answer = BIG_NUM
    
    q = Queue()
    
    q.put((currentRow, currentCol, ""))
    
    while not q.empty():
        row, col, presses = q.get()
        
        if (row, col) == (destRow, destCol):
            rec = cheapestRobot(presses + "A", 26)
            answer = min(answer, rec)
            continue
            
        if (row, col) == Num.ERROR.value:
            continue
        
        else:
            if row < destRow:
                q.put((row + 1, col, presses + "v"))
            elif row > destRow:
                q.put((row - 1, col, presses + "^"))
                
            if col < destCol:
                q.put((row, col + 1, presses + ">"))
            elif col > destCol:
                q.put((row, col - 1, presses + "<"))
    
    return answer

def processCodeTwo(code):
    result = 0
    
    currentRow, currentCol = Num.A.value
    
    for char in code:
        nextRow, nextCol = Num.getNum(char).value
        result += cheapest(currentRow, currentCol, nextRow, nextCol)
        currentRow = nextRow
        currentCol = nextCol
    
    return result * numericPart(code)

def partTwo():
    answer = 0
    
    for code in codes:
        answer += processCodeTwo(code)
    
    return answer

if __name__ == "__main__":    
    print(f'The answer for part one is: {partOne()}')
    print(f'The answer for part two is: {partTwo()}')