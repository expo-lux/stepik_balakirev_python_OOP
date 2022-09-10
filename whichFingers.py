import math

def whichFingers(x: int) -> str:
    if (x - 3) % 4 == 0:
        return "Middle finger"
    elif (x - 1) % 8 == 0:
        return "Thumb"
    elif (x - 5) % 8 == 0:
        return "Little finger"
    elif math.floor(x/4) % 2 == 0:
        return "Index finger"
    elif math.floor(x/4) % 2:
        return "Ring finger"

print(whichFingers(10))
print(whichFingers(20))
print(whichFingers(30))
print(whichFingers(50))
print(whichFingers(17))
print(whichFingers(19))
print(whichFingers(21))