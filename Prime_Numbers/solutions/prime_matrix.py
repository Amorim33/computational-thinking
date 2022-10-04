# B. Prime Matrix
# https://codeforces.com/problemset/problem/271/B

# 10^5
maxNumber = 100010

primeFlags = [True for i in range(maxNumber + 1)]
def sieve_of_eratosthenes(n):
    # 0 and 1 are not prime numbers
    primeFlags[0] = False
    primeFlags[1] = False
    p = 2
    while (p * p <= n):
        if (primeFlags[p] == True):
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                primeFlags[i] = False
        p += 1
 
 

n, m = map(int, input().split())


matrix = [[0 for x in range (m)] for y in range(n)]

for i in range(n):
    line = input().split()
    for j in range(m):
        matrix[i][j] = int(line[j])


sieve_of_eratosthenes(maxNumber)

lineOperationCount = 0
columnOperationCount = 0

lastLineOperationCount = 0
lastColumnOperationCount = 0

minLineOperationsCount = 999999
minColumnOperationsCount = 999999

for i in range(n):
    operationsCount = 0
    for j in range(m):
        currentNumber = matrix[i][j]
        while True:  
            if primeFlags[currentNumber]:
                break
            currentNumber += 1
            operationsCount += 1

    lineOperationCount = operationsCount
    if lineOperationCount < minLineOperationsCount:
        minLineOperationsCount = lineOperationCount


for j in range(m):
    operationsCount = 0
    for i in range(n):
        currentNumber = matrix[i][j]

        while True:
            if primeFlags[currentNumber]:
                break
            currentNumber += 1
            operationsCount += 1

    columnOperationCount = operationsCount
    if columnOperationCount < minColumnOperationsCount:
        minColumnOperationsCount = columnOperationCount



resp = min(minLineOperationsCount, minColumnOperationsCount)
print(resp)

