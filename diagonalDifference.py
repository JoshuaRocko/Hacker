# https://www.hackerrank.com/challenges/diagonal-difference/problem

n = int(input())
arrayN = []
diagA = 0
diagB = 0
for i in range(n):
    arrayN.append(input().split(' '))

# print(arrayN)

for i in range(n):
    # print(f'arrayN[{i}][{i}]: {arrayN[i][i]}')
    diagA += int(arrayN[i][i])
j = 0
for i in range(n-1, -1, -1):
    # print(f'arrayN[{j}][{i}]: {arrayN[j][i]}')
    diagB += int(arrayN[j][i])
    j += 1

# print(f'DiagA: {diagA}')
# print(f'DiagB: {diagB}')
print(abs(diagA-diagB))
