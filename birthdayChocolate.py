def birthday(squares, day, month):
    i = 0; j = 0
    number_of_ways = 0
    for i in range(len(squares)-month):
        #print(i)
        sumAux = 0
        for j in range(i,i+month,1):
            #print(f'i = {i}  j = {j}')
            sumAux += squares[j]
        if sumAux == day:
            #print(f'suma = {sumAux}')
            number_of_ways += 1
    return number_of_ways


n = int(input())

squares = list(map(int, input(' ').split()))

day_month = list(map(int, input(' ').split()))

print(birthday(squares, day_month[0], day_month[1]))