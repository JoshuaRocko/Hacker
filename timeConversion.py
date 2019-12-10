# https://www.hackerrank.com/challenges/time-conversion/problem

hour12 = input()

if hour12.find('PM') >= 0:
    hour12 = hour12.replace('PM', '')
    hour = hour12.split(':')
    if not '12' in hour[0]:
        hour[0] = int(hour[0]) + 12
elif hour12.find('AM') >= 0:
    hour12 = hour12.replace('AM', '')
    hour = hour12.split(':')
    if '12' in hour[0]:
        hour[0] = hour[0].replace('12', '00')

print(f'{hour[0]}:{hour[1]}:{hour[2]}')

# print(hour)
