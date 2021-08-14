# Kattis-Python-Solutions
# Coded Daniyal Arteshdar 
import math
for i in range(int(input())):
    xy = [int(a) for a in input().split()]
    x, y = xy[0], xy[1]
    h1 = (y + x - math.sqrt(y * y - x * y + x * x)) / 6.0
    h2 = (y + x + math.sqrt(y * y - x * y + x * x)) / 6.0
    if h1 < 0: ans = 2 * (y - 2 * h2) * (x - 2 * h2)
    elif h2 < 0: ans = h1 * (y - 2 * h1) * (x - 2 * h1)
    else: ans = max(h1 * (y - 2 * h1) * (x - 2 * h1), 2 * (y - 2 * h2) * (x - 2 * h2))
print(ans) 
