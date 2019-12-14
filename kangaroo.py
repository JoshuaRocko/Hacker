# https://www.hackerrank.com/challenges/kangaroo/problem

def kangaroo (x1, v1, x2, v2):
    if (x1 == x2 and v1 == v2):
        return "YES"
    if (x1 > x2 and v1 > v2) or (x2 > x1 and v2 > v1) or (v2 == v1 and (x2 > x1 or x1 > x2)):
        return "NO"
    if abs((x1-x2)/(v2-v1)).is_integer():
        return "YES"
    else:
        return "NO"

inpuT = input().split(' ')
x1 = int(inpuT[0])
v1 = int(inpuT[1])
x2 = int(inpuT[2])
v2 = int(inpuT[3])

print(kangaroo(x1, v1, x2, v2))