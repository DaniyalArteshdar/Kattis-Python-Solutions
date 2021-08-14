# Kattis-Python-Solutions
# Coded Daniyal Arteshdar
x = input().split(';')
c = 0

for i in x :
    if ( '-' in i ) :
        ww = list(map(int, i.split('-')))
        c += ww[1] - ww[0] +1
    else:
        c += 1

print(c)
