#Create a custom range function

def frange(start, stop=None, step=None):
    if stop == None:
        stop = start + 0.0
        start = 0.0
    if step == None:
        step = 1.0
    while True:
        if step > 0 and start >= stop:
            break
        elif step < 0 and start <= stop:
            break
        yield ("%g" % start) # return float number
        start = start + step
print ("Printing float range")
floatList = frange(0.5, 1.0, 0.1)
for num in floatList:
    print (num)


#Create range() over character or alphabet

print ("""Generates the characters from `a` to `z`, inclusive.""")
def character_range(char1, char2):
    for char in range(ord(char1), ord(char2)+1):
        yield (char)
for letter in character_range('a', 'z'):
    print( chr(letter), end=", " )
