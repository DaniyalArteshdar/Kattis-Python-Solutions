# Kattis-Python-Solutions
# Coded by Daniyal Arteshdar

g, s, c = map(int, input().split())
total = (g*3) + (s*2) + (c)
result = " "
rresult = " "

if total > 7 :
    result ="Province or"
elif total > 4 :
    result ="Duchy or"
elif total > 1 :
    result ="Estate or"


if total > 5 :
    rresult = "Gold"
elif total > 2 :
    rresult = "Silver"
else:
    rresult ="Copper"

print(result , rresult)
