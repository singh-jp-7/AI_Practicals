import math
n = int(input("enter number of direction to move"))
x1 = 0
y1 = 0
x2 = 0
y2 = 0
for i in range(n):
    dirn = input("enter direction (eg:LEFT,UP,DOWN,RIGHT) ")
    step = input("enter no of steps in that directions")
    steps = int(step)
    if (dirn == "LEFT"):
        x2 = x2 - steps
        y2 = y2
    elif (dirn == "UP"):
        x2 = x2
        y2 = y2 + steps
    elif (dirn == "RIGHT"):
        x2 = x2 + steps
        y2 = y2
    elif (dirn == "DOWN"):
        x2 = x2
        y2 = y2 - steps
temp=((x2-x1)*(x2-x1)) + ((y2-y1)*(y2-y1))
distance=math.sqrt(temp)
print("distance from tarting point = ", round(distance), "steps", end='')