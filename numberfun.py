# Kattis-Python-Solutions
# Coded by Daniyal Arteshdar 
for i in range(int(input())) :
    a, b, c = map(int,input().split())
    if (a + b == c) or (b + a == c) :
        print('possible')
    elif (a - b == c) or (b - a == c) :
        print('possible')
    elif (a * b == c) or (b * a == c):
        print('possible')
    elif (a / b == c) or (b / a == c):
        print('possible')
    else:
        print('impossible')
