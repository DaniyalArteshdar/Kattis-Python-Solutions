# Kattis-Python-Solutions
# Coded by Daniyal Arteshdar
g = [int(i) for i in input().split()]
e = [int(i) for i in input().split()]
if sum(g) > sum(e): print("Gunnar")
elif sum(g) < sum(e): print("Emma")
else: print("Tie")
