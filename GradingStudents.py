# https://www.hackerrank.com/challenges/grading/problem

n = int(input())
grades = []
for i in range(n):
    grades.append(int(input()))
    if grades[i] < 38:
        continue
    elif grades[i] % 5 > 2:
        grades[i] = grades[i] + (5-(grades[i] % 5))

for i in range(n):
    print(grades[i])
