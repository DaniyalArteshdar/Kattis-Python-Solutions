# Kattis-Python-Solutions
#Coded by Daniyal Arteshdar
import datetime
a = input().split()
a = [int(i) for i in a]
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
ans = datetime.datetime(2009, a[1], a[0]).weekday()
print(days[ans])
