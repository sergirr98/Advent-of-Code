import re

regisitries = []
program = []

standardJump = 2

def generateInput():
    
    regisitries.clear()
    program.clear()
    
    firstPart = True
    
    with open('./2024/17/input.txt', 'r') as file:
        for line in file:
            if line == '\n':
                firstPart = False
                continue
            
            numbers = re.findall(r'[-]?\d+', line)
            numbers = [int(x) for x in numbers]
            
            if firstPart:
                regisitries.extend(numbers)
            else:
                program.extend(numbers)
                
    return regisitries, program

def getComboOperand(operand):
    
    if operand <= 3:
        return operand
    if operand == 4:
        return regisitries[0]
    if operand == 5:
        return regisitries[1]
    if operand == 6:
        return regisitries[2]

def processInstruction(i):
    
    instruction = program[i]
    operand = program[i + 1]
    
    if instruction == 0:
        numerator = regisitries[0]
        denominator = 2 ** getComboOperand(operand)
        
        regisitries[0] = numerator // denominator
        return standardJump, ''
    
    if instruction == 1:
        regisitries[1] = regisitries[1] ^ operand
        return standardJump, ''
    
    if instruction == 2:
        regisitries[1] = getComboOperand(operand) % 8
        return standardJump, ''
        
    if instruction == 3:
        return operand, ''
    
    if instruction == 4:
        regisitries[1] = regisitries[1] ^ regisitries[2]
        return standardJump, ''
    
    if instruction == 5:
        out = getComboOperand(operand) % 8
        return standardJump, out
    
    if instruction == 6:
        numerator = regisitries[0]
        denominator = 2 ** getComboOperand(operand)
        
        regisitries[1] = numerator // denominator
        return standardJump, ''
    
    if instruction == 7:
        numerator = regisitries[0]
        denominator = 2 ** getComboOperand(operand)
        
        regisitries[2] = numerator // denominator
        return standardJump, ''

def run(a = 0):
    
    generateInput()
    
    if a != 0:
        regisitries[0] = a
    
    i = 0
    
    output = []
    
    while i < len(program):
        jump, out = processInstruction(i)
        
        if out != '':
            output.append(out)
            
        if program[i] == 3 and regisitries[0] != 0:
            i = jump
        else:
            i += standardJump
    
    return output

def partOne():
    
    output = run()
    
    return ','.join([str(i) for i in output])

def get_best_quine_input(cursor, sofar):
    for candidate in range(8):
        if run(sofar * 8 + candidate) == program[cursor:]:
            if cursor == 0:
                return sofar * 8 + candidate
            ret = get_best_quine_input(cursor - 1, sofar * 8 + candidate)
            if ret is not None:
                return ret
    return None

def partTwo():
    return get_best_quine_input(len(program) - 1, 0)

if __name__ == "__main__":
    print(f'The answer for part one is: {partOne()}')
    print(f'The answer for part two is: {partTwo()}')