connections = set()
computers = set()
        
def parseLine(line):
    compA = line[:2]
    compB = line[3:5]
    
    computers.add(compA)
    computers.add(compB)
    
    return compA, compB

def readInput():
    
    with open('./2024/23/input.txt', 'r') as file:
        for line in file:
            connections.add(parseLine(line))
    
    return

def partOne():
    
    connDict = dict()
    trios = set()
    
    for c in computers:
        connDict[c] = []
    
    for connection in connections:
        connDict[connection[0]].append(connection[1])
        connDict[connection[1]].append(connection[0])
    
    for compA in connDict:
        if 't' == compA[:1]:
            for compB in connDict[compA]:
                for compC in connDict[compB]:
                    for compD in connDict[compC]:
                        if compD == compA:
                            trio = tuple(sorted((compA, compB, compC)))
                            trios.add(trio)
    
    return len(trios)

def partTwo():
    
    answer = set()
    
    connDict = dict()
    networks = []
    
    for c in computers:
        connDict[c] = []
        
        net = set()
        net.add(c)
        networks.append(net)
    
    for connection in connections:
        connDict[connection[0]].append(connection[1])
        connDict[connection[1]].append(connection[0])
        
    for computer in computers:
        for net in networks:
            
            connected = True
            
            for c in net:
                if c not in connDict[computer]:
                    
                    connected = False
                    break
            
            if connected:
                net.add(computer)
                
    for net in networks:
        if len(net) > len(answer):
            answer = net
    
    answer = sorted(answer)
    
    return ",".join(answer)

if __name__ == "__main__":
    
    readInput()
    
    print(f'The answer for part one is: {partOne()}')
    print(f'The answer for part two is: {partTwo()}')