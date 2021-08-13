# Kattis-Solutions
# Coded by Daniyal Arteshdar
m, s = 0, 0
for i in range(int(input())):
    mins, secs = input().split()
    m, s = int(m) + int(mins), int(s) + int(secs)
s = s / 60
if s/m == 1 or s/m < 1:
    print("measurement error")
else:
print('{:.9f}'.format(s/m))
