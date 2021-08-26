# Kattis-Python-Solutions
# Coded by Daniyal Arteshdar

price = float(input())
raw = int(input())
c = 0
for i in range(raw):
    a, b = map(float, input().split())
    c += a * b * price

print(c)
