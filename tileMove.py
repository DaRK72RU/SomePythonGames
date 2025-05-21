def up():
    tileField[y][x] = []
    tileField[y-1][x] = '@'

def down():
    tileField[y][x] = []
    tileField[y+1][x] = '@'

def left():
    tileField[y][x] = []
    tileField[y][x-1] = '@'

def right():
    tileField[y][x] = []
    tileField[y][x+1] = '@'

tileField = [[[] for i in range(9)] for i in range(9)]
x = y = 4
mx = my = 8
nx = ny = 0
tileField[y][x] = '@'
for i in tileField:
    print(i)
print('----------------------------------------')
inp = 1
while inp != 0:
    inp = input()
    if inp == 'w' and y > ny:
        up()
        y -= 1
        for i in tileField:
            print(i)
    elif inp == 'a' and x > nx:
        left()
        x -= 1
        for i in tileField:
            print(i)
    elif inp == 's' and y < my:
        down()
        y += 1
        for i in tileField:
            print(i)
    elif inp == 'd' and x < mx:
        right()
        x += 1
        for i in tileField:
            print(i)
    else:
        for i in tileField:
            print(i)