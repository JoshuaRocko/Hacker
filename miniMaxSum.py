#https://www.hackerrank.com/challenges/mini-max-sum/problem

arr = list(map(int, input().split(' ')))

arr.sort()
maxi = 0
mini = 0

for i in range(1,5):
    maxi += arr[i]
for i in range(0,4):
    mini += arr[i]

print(f'{mini} {maxi}')