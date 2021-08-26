# Kattis-Python-Solutions
# Coded by Daniyal Arteshdar

letters = list ( input ( ) )
uniqueLetters = set ( letters )
canGuess = len ( letters ) == len ( uniqueLetters )
if canGuess :
    print ( "1" )
else :
print ( "0" )
