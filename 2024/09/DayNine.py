from enum import Enum

class Block(Enum):
    Empty = -1

elems = []

def getBlocks():
    blocks = []
    
    for i, elem in enumerate(elems):
        if i % 2 == 0:
            for j in range(elem):
                blocks.append(i // 2)
        else:
            for j in range(elem):
                blocks.append(Block.Empty)
    
    return blocks

def orderBlocks(blocks):
    
    indexStart = 0
    indexEnd = len(blocks) - 1
    
    while blocks[indexStart] != Block.Empty:
        indexStart += 1
    
    while blocks[indexEnd] == Block.Empty:
        indexEnd -= 1
    
    while indexStart < indexEnd:
        blocks[indexStart] = blocks[indexEnd]
        blocks[indexEnd] = Block.Empty
        
        while blocks[indexStart] != Block.Empty:
            indexStart += 1
            
        while blocks[indexEnd] == Block.Empty:
            indexEnd -= 1
    
    return blocks

def moveElement(blocks, id, indexEnd):
    spaceCounter = 0
    
    size = 0
    
    while blocks[indexEnd - size] == id:
        size += 1
    
    for i, elem in enumerate(blocks):
        if i == indexEnd:
            return
        
        if elem == Block.Empty:
            spaceCounter += 1
        else:
            spaceCounter = 0
            
        if spaceCounter == size:
            for j in range(size):
                blocks[i - j] = id
                blocks[indexEnd - j] = Block.Empty
            
            return
    

def orderBlocksPartTwo(blocks):
    idsChecked = set()
    
    indexEnd = len(blocks) - 1
    
    while indexEnd >= 0:
        if blocks[indexEnd] != Block.Empty and blocks[indexEnd] not in idsChecked:
            id = blocks[indexEnd]
            idsChecked.add(id)
            moveElement(blocks, id, indexEnd)
        
        indexEnd -= 1
    
    return blocks

def partOne():
    answer = 0
    
    blocks = getBlocks()
    
    blocks = orderBlocks(blocks)
    
    for i, elem in enumerate(blocks):
        if elem == Block.Empty:
            break
        
        answer += i * elem
    
    return answer

def partTwo():
    answer = 0
    
    blocks = getBlocks()
    
    blocks = orderBlocksPartTwo(blocks)
    
    for i, elem in enumerate(blocks):
        if elem != Block.Empty:
            answer += i * elem
    
    return answer

if __name__ == "__main__":
    
    with open('./2024/09/input.txt', 'r') as file:
        for line in file:
            for i in range(len(line) - 1):
                elems.append(int(line[i]))
    
    print(f'The answer for part one is: {partOne()}')
    print(f'The answer for part two is: {partTwo()}')