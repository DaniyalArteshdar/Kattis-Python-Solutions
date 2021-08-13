# Kattis-Python-Solutions
# Coded by Daniyal Arteshdar 
for i in range(int(input())):
    contestant = input().split()
    if (int(contestant[1].split('/')[0]) >= 2010 or int(contestant[2].split('/')[0]) >= 1991): ans = 'eligible'
    elif int(contestant[3]) > 40: ans = 'ineligible'
    else: ans = 'coach petitions'
print(contestant[0], ans)
