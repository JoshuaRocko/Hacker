#https://www.hackerrank.com/challenges/plus-minus/problem

n = int(input())
arrayN = input().split(' ')
nPositve = 0
nNegative = 0
nZero = 0
for i in range(n):
    if int(arrayN[i]) > 0:
        nPositve += 1
    elif int(arrayN[i]) < 0:
        nNegative += 1
    elif int(arrayN[i]) == 0:
        nZero += 1

print(nPositve/n)
print(nNegative/n)
print(nZero/n)