
numberCandles = int(input())

heightCandles = list(map(int, input().split(' ')))

maxHeight = max(heightCandles)

print(heightCandles.count(maxHeight))