# Kattis-Python-Solutions
# Coded by Daniyal Arteshdar 
from collections import Counter
hand = input().split()
cards = []
for card in hand:
    cards.append(card[:1])
counts = (Counter(cards))
print(max(counts.values()))
