# Kattis-Python-Solutions
# Coded Daniyal Atreshdar 
a, b = map(int, input().split())
c = a - b
x = 0
for i in range (b) :
    point = int(input())
    x = point + x

if c != 0:
    maxave = (x + (3*c)) / a
    minave = (x - (3*c)) / a
else:
    maxave = x / a
    minave = maxave

print(minave, maxave)
