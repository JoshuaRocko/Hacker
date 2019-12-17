def breakingRecords(scores):
    highest = scores[0]
    lowest = scores[0]
    records = []
    records.append(0)
    records.append(0)
    for i in scores:
        if i > highest:
            highest = i
            records[0] += 1
        if i < lowest:
            lowest = i
            records[1] += 1
    return records

n = int(input())

scores = list(map(int, input().split(' ')))

records = breakingRecords(scores)

print(f'{records[0]} {records[1]}')
