# https://www.hackerrank.com/challenges/migratory-birds/problem


def migratoryBirds(array):
    idBirds = []
    for i in array:
        if idBirds.count(i) == 0:
            idBirds.append(i)
    idBirds.sort()
    counts = []
    aux = []
    for i in idBirds:
        c = array.count(i)
        aux.append(i)
        aux.append(c)
        counts.append(list(aux))
        aux.clear()
    maxC = 0
    maxSightings = 0
    for i in range(len(counts)):
        if counts[i][1] > maxSightings:
            maxC = counts[i][0]
            maxSightings = counts[i][1]
    return maxC


n = int(input())

array = list(map(int, input().split()))

print(migratoryBirds(array))
