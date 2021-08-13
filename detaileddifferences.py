# Kattis-Python-Solutions
# Coded by Daniyal Arteshdar
for i in range ( int ( input ( ) ) ) :
    text1 = input ( )
    text2 = input ( )
    diff = ''
    for carc1, carc2 in zip(text1, text2) :
        if carc1 == carc2 :
            diff += '.'
        else:
            diff += '*'

    print(text1)
    print(text2)
    print(diff)
    print('')
