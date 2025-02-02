secrets = []

prices = []

changes = []

def generateInput():
    with open('./2024/22/input.txt', 'r') as file:
        for line in file:
            l = int(line)
            secrets.append(l)

def mix(num, secret):
    return num ^ secret

def prune(secret):
    return secret % 16777216

def step(secret):
    # Step one
    num = secret * 64
    secret = mix(num, secret)
    secret = prune(secret)
    
    # Step two
    num = secret // 32
    secret = mix(num, secret)
    secret = prune(secret)
    
    # Step three
    num = secret * 2048
    secret = mix(num, secret)
    secret = prune(secret)
    
    return secret

def processSecret(secret):
    
    price = []
    change = []
    
    price.append(secret % 10)
    
    for i in range(2000):
        secret = step(secret)
        
        price.append(secret % 10)
        change.append(price[-1] - price[-2])
    
    prices.append(price)
    changes.append(change)
    
    return secret

def partOne():
    
    generateInput()
    
    answer = 0
    
    for secret in secrets:
        answer += processSecret(secret)
    
    return answer

def partTwo():
    
    answer = 0
    
    bananasDic = dict()
    
    for i, change in enumerate(changes):
        
        sequence = dict()
        
        for c in range(3, len(change)):
            
            key = (change[c - 3], change[c - 2], change[c - 1], change[c])
            
            if key not in sequence:
                sequence[key] = prices[i][c + 1]

        
        for k, v in sequence.items():
            if k in bananasDic:
                bananasDic[k] += v
            else:
                bananasDic[k] = v

    answer = max(bananasDic.values())
    
    return answer

if __name__ == "__main__":    
    print(f'The answer for part one is: {partOne()}')
    print(f'The answer for part two is: {partTwo()}')