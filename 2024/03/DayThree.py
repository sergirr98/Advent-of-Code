import re

lines = []

def partOne():
    answer = 0
    
    for line in lines:
        x = re.findall(r"mul\([0-9]+,[0-9]+\)", line)
        for mul in x:
            nums = re.findall("[0-9]+", mul)
            nums = [int(y) for y in nums]
            answer += (nums[0] * nums[1])
    
    return answer

def partTwo():
    answer = 0
    
    enabled = True
    
    for line in lines:
        x = re.findall(r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", line)
        for elem in x:
            if elem == "do()":
                enabled = True
            elif elem == "don't()":
                enabled = False
            elif enabled:
                nums = re.findall("[0-9]+", elem)
                nums = [int(y) for y in nums]
                answer += (nums[0] * nums[1])
    
    return answer

if __name__ == "__main__":
    
    with open('./2024/03/input.txt', 'r') as file:
        for line in file:
            lines.append(line)
    
    print(f'The answer for part one is: {partOne()}')
    print(f'The answer for part two is: {partTwo()}')